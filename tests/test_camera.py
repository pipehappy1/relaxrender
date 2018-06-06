import unittest
import numpy as np

import relaxrender.camera as c
import relaxrender.triangle as t
import relaxrender.points as rp

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.pos = np.array([1.0, 1.0, 1.0])
        self.up = np.array([1.0, 1.0, 0])
        self.right = np.array([1.0, -1.0, 0])

    def test_bad_direction(self):
        pos = np.array([1.0, 1.0, 1.0])
        up = np.array([1.0, 1.0, 0])
        right = np.array([1.0, 0.0, 0])

        with self.assertRaises(ValueError):
            c.CameraBase(pos, up, right)

        with self.assertRaises(NotImplementedError):
            camera = c.CameraBase(self.pos, self.up, self.right)
            camera.sample_vector()

    def test_relocate_camera(self):
        pos = self.pos
        up = self.up
        right = self.right
        camera = c.CameraBase(pos, up, right)

        tris = t.Triangles()
        tris.add_triangle(t.Triangle(rp.Point3D(1., 1, -5.0),
                               rp.Point3D(1, 0, -5.0),
                               rp.Point3D(2, 0, -5.0)))

        relocated_tris = camera.relocate_world_by_camera(tris)
        tri0 = relocated_tris[0]

        expected_tri = t.Triangle(rp.Point3D(0,0,-6),
                                  rp.Point3D(1/np.sqrt(2),-1/np.sqrt(2),-6),
                                  rp.Point3D(np.sqrt(2),0,-6))

        self.assertTrue(tri0 == expected_tri)

    def test_perspective_sample(self):
        h_angle = np.pi/2
        v_angle = np.pi/2
        camera = c.PerspectiveCamera(self.pos, self.up, self.right, h_angle, v_angle)
        samples, xy = camera.sample_vector(2)

    def test_orthogonal_sample(self):
        width = 2
        height = 2
        camera = c.OrthogonalCamera(self.pos, self.up, self.right, width, height)
        samples, xy = camera.sample_vector(2)
