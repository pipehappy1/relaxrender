import unittest

import relaxrender.points as rp
import relaxrender.color as color

class TestPoints(unittest.TestCase):

    def test_addpoint(self):
        points = rp.Points()
        points.add_point(rp.Point(0.5, 0.5, 0.5, None,
                                  color.Color.place_holder(),
                                  rp.Vector.place_holder()))

        points.add_point(rp.Point(0.1, 0.5, 0.5, None,
                                  color.Color.place_holder(),
                                  rp.Vector.place_holder()))

        self.assertEqual(points.data[:points.cindex].shape, (2, 15))
        self.assertEqual(points.data[0,0], 0.5)
        self.assertEqual(points.data[0,1], 0.5)
        self.assertEqual(points.data[0,2], 0.5)
        self.assertEqual(points.data[1,0], 0.1)
        self.assertEqual(points.data[1,1], 0.5)
        self.assertEqual(points.data[1,2], 0.5)

        

        
