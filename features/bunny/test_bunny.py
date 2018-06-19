from features.bunny import light
from features.bunny.objloader import OBJ
import pickle
import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.freeglut import *
from pygame.locals import *

def step1():
    fn = "obj.pkl"
    if 1 == 1:
        obj = OBJ("", "bunny.obj", swapyz=True)
        obj.create_bbox()

        with open(fn, 'wb') as f:  # open file with write-mode
            pickle.dump(obj, f)  #picklestring = pickle.dumps(summer)
    else:
        with open(fn, 'rb') as f:
            obj = pickle.load(f)

    pygame.init()
    # 设置成一样的 这样 glOrtho 就简单些
    viewport = (600, 600)
    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

    light.setup_lighting()
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, -100, 0.0)) # 指的是光的朝向

    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)  # most obj files expect to be smooth-shaded

    obj.create_gl_list()

    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    #gluPerspective(60.0, width / float(height), 1, 100.0)
    cam=light.camera
    #cam.Ortho.params=cam.Ortho.params*15
    cam.Ortho.bbox[:] = cam.Ortho.bbox * 13
    cam.Ortho.nf[:] = cam.Ortho.nf * 20
    glOrtho(*cam.Ortho.params)

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)

    rx, ry = (0, 0)
    tx, ty = (0, 0)
    zpos = 5
    rotate = move = False
    while 1:
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4:
                    zpos = max(1, zpos - 1)
                elif e.button == 5:
                    zpos += 1
                elif e.button == 1:
                    rotate = True
                elif e.button == 3:
                    move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    rotate = False
                elif e.button == 3:
                    move = False
            elif e.type == MOUSEMOTION:
                #p(e.rel)
                i, j = e.rel
                if rotate:
                    rx -= i
                    ry -= j
                if move:
                    tx += i
                    ty -= j

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()


        # RENDER OBJECT
        glTranslate(tx / 20., ty / 20., - zpos)
        glRotate(ry/5, 1, 0, 0)
        glRotate(rx/5, 0, 0, 1)

        s = [ 10/obj.bbox_half_r ]*3
        glScale(*s)

        t = -obj.bbox_center
        glTranslate(*t)

        glCallList(obj.gl_list)

        pygame.display.flip()
step1()
