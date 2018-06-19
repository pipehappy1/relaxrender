import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

from PIL import Image
from PIL import ImageOps

offset = 0
count=20

class Teapot:
    def display(self):
        global offset
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 0, 0, 1)
        glTranslatef(offset,0,0)
        glPushMatrix()
        gluLookAt(0, 6, 8, 0, 0, 0, 0, 1, 0)
        glutSolidTeapot(2.5)
        glPopMatrix()     
        glFlush()


    def reshape(self,w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.0 * w / h, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


#    def keyboard(self,key, x, y): 
#        if key == chr(32): sys.exit(0)

    def idle(self):    
        global offset
        global count
        global window_id
        time.sleep(0.1)
        count=count-0.1        
        if (offset < -0.3):
            offset = 0
        elif (offset > 0.3):
            offset = 0.3-offset
        elif (offset < 0):
            offset = offset - 0.01
        elif (offset <= 0.3 ):
            offset=offset+0.01
            
        self.display()

    def init(self):
        global window_id
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(500, 400)
        window_id = glutCreateWindow('teapot')
        glutReshapeFunc(self.reshape)
#        glutKeyboardFunc(self.keyboard)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle)


    def main(self):
        global count
        self.init()
        while (count > 0):
            self.idle()
            glutMainLoopEvent()


    def save(self):
        self.init()
        glutMainLoopEvent()
        time.sleep(1)
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        data = glReadPixels(0, 0, 500, 400, GL_RGBA, GL_UNSIGNED_BYTE)
        image = Image.frombytes("RGBA", (500, 400), data)
        image = ImageOps.flip(image)
        image.save("teapot.png", "PNG")


#if __name__ == "__main__":
#    t=Teapot()
#    t.main()
