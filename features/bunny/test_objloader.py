import unittest
import features.bunny.objloader as ol
import pygame
from pygame.locals import *

class TestObjLoader(unittest.TestCase):
    def test_OBJ(self):
        obj = ol.OBJ("", "bunny.obj", swapyz=True)
        obj.create_bbox()
        pygame.init()
        viewport = (600, 600)
        pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
        obj.create_gl_list()
