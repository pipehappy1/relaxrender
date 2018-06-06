import unittest

import relaxrender.color as color

class TestCamera(unittest.TestCase):

    def test_color(self):
        # bad color class
        with self.assertRaises(ValueError):
            color.Color('unknown_color_mode', 1, 2, 3, 4)
        
