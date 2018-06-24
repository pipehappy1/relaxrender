import unittest
import numpy as np

import relaxrender.triangle as tri
import relaxrender.points as rp
import relaxrender.color as color
import relaxrender.context as ctx

class TestTriangles(unittest.TestCase):

    def test_addpoint(self):
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
        
        self.assertEqual(tr1.cindex, 1)

    def test_size(self):
        tr1 = tri.Triangles()

        p1 = np.array([0,0,0])
        p2 = np.array([1,0,0])
        p3 = np.array([1,1,0])

        tr1.append_tri(p1, p2, p3)

        self.assertEqual(tr1.size(), 1)

        p1 = np.array([0,0,0])
        p2 = np.array([1,0,0])
        p3 = np.array([1,1,0])
        tr1.append_tri(p1, p2, p3)

        self.assertEqual(tr1.size(), 2)
	def test_triangle(self):
        tctx = ctx.Context()
        if tctx.triangle_right_hand_norm:
            p1 = rp.Point3D(0, 0, 0)
            p2 = rp.Point3D(1, 0, 0)
            p3 = rp.Point3D(0, 1, 0)
        else:
            p1 = rp.Point3D(0, 0, 0)
            p2 = rp.Point3D(0, 1, 0)
            p3 = rp.Point3D(1, 0, 0)

        ttri = tri.Triangle(p1, p2, p3)

        self.assertTrue(ttri.verify())

    def test_read(self):
        tr1 = tri.Triangles()

        p1 = np.array([0,0,0])
        p2 = np.array([1,0,0])
        p3 = np.array([1,1,0])

        tr1.append_tri(p1, p2, p3)

        with self.assertRaises(NotImplementedError):
            tr1.items()

        self.assertTrue(abs(np.linalg.norm(tr1[0].p1.data - p1)) < 1e-6)

    

    def test_easy_add(self):
        p1 = np.array([0,0,0])
        p2 = np.array([1,0,0])
        p3 = np.array([1,1,0])
        
        tr1 = tri.Triangles()
        tr1.append_tri(p1, p2, p3)

        self.assertTrue(abs(np.linalg.norm(tr1[0].p1.data - p1)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[0].p2.data - p2)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[0].p3.data - p3)) < 1e-6)


        p1 = np.array([0,0,0])
        p2 = np.array([1,0,0])
        p3 = np.array([1,1,0])
        p4 = np.array([0,1,0])
        
        tr1 = tri.Triangles()
        tr1.append_rct(p1, p2, p3, p4)
        self.assertTrue(abs(np.linalg.norm(tr1[0].p1.data - p1)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[0].p2.data - p2)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[0].p3.data - p3)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[1].p1.data - p1)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[1].p2.data - p3)) < 1e-6)
        self.assertTrue(abs(np.linalg.norm(tr1[1].p3.data - p4)) < 1e-6)
        
        
    def test_get_triangle(self):
        p1 = rp.Point3D(0, 0, 0)
        p2 = rp.Point3D(0, 1, 0)
        p3 = rp.Point3D(1, 0, 0)

        tri1 = tri.Triangle(p1, p2, p3)

        p1 = rp.Point3D(0, 0, 0)
        p2 = rp.Point3D(0, 0.5, 0)
        p3 = rp.Point3D(0.5, 0, 0)

        tri2 = tri.Triangle(p1, p2, p3)

        tris = tri.Triangles()
        tris.add_triangle(tri1)
        tris.add_triangle(tri2)

        trir1 = tris[0]
        trir2 = tris[1]
        self.assertEqual(trir1, tri1)
        self.assertEqual(trir2, tri2)
        
