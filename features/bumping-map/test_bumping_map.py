import unittest

import bumping_map as bp

class TestBumpingMap(unittest.TestCase):
    def test_bumping_map(self):
        self.assertEqual(bp.draw(),1)
        