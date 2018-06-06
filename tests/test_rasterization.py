import unittest

import relaxrender.triangle as tri
import relaxrender.points as rp
import relaxrender.color as color
import relaxrender.rasterization as raster
import relaxrender.context as context

class TestRasterization(unittest.TestCase):

    def test_rasterize(self):
        p1 = rp.Point(0.5, 0.5, 0.5, None,
                       color.Color.place_holder(),
                       rp.Vector.place_holder())

        p2 = rp.Point(0.0, 0.0, 0.0, None,
                       color.Color.place_holder(),
                       rp.Vector.place_holder())

        p3 = rp.Point(0.5, 0.0, 0.5, None,
                       color.Color.place_holder(),
                       rp.Vector.place_holder())

        tr1 = tri.Triangles()
        tr1.add_triangle(tri.Triangle(p1, p2, p3))

        ctx = context.Context()
        render = raster.SimpleRaster(ctx)
        render.rasterize(tr1)

        #self.assertEqual(tr1.cindex, 1)
