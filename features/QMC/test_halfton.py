import unittest
import halftone

class Testhalftone(unittest.TestCase):
    def testhalftone_gray(self):
        h = halftone.Halftone('1.jpg')
        h.make(style='grayscale',filename_add='1')
    def testOthers(self):
        h = halftone.Halftone('1.jpg')
        h.make(style='color',filename_add='4',percentage=100,antialias=True)
        h.make(style='color',filename_add='5',percentage=0,antialias=True)
