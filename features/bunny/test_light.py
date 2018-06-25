import unittest
import features.bunny.light as lt
import pygame
from pygame.locals import *



class TestLight(unittest.TestCase):
    def test_setlighting(self):
        pygame.init()
        viewport = (600, 600)
        pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
        lt.setup_lighting()

        cam = lt.camera
        cam.Ortho.bbox[:] = cam.Ortho.bbox * 13
        cam.Ortho.nf[:] = cam.Ortho.nf * 20


