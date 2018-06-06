import unittest

import numpy as np
from relaxrender.example_meshs import *
from relaxrender.math import *
from relaxrender.points import *
from relaxrender.triangle import *


class TestMath(unittest.TestCase):

    def test_dist(self):
        p1 = Point3D(1, 0, 0)
        p2 = Point3D(2, 0, 0)
        self.assertTrue(np.abs(dist(p1, p2) - 1) < 1e-6)

    def test_sphere_sampling(self):
        x, y, z = sphere_sampling(1)
        tsum = np.sum((x**2, y**2, z**2))
        # test for the output is on the uniform sphere.
        self.assertTrue(np.abs(np.sqrt(tsum) - 1) < 1e-4)

        sample_size = int(1e6)
        res = sphere_sampling(sample_size)

        upper_count = np.sum(res[:,2] > 0.5)
        lower_count = np.sum(res[:,2] < -0.5)

        # test for the distributio is even on two side so the sphere.
        self.assertTrue(np.abs(upper_count-lower_count)/sample_size < 0.01 )


    def test_line_in_triangle(self):
        # test for the line is parallel to the plane.
        ray = Vector(Point3D(0, 0, 0), Point3D(1, 0, 0))
        tri = Triangle(Point3D(0, 0, 1),
                       Point3D(1, 0, 1),
                       Point3D(0, 1, 1))
        
        self.assertTrue(line_in_triangle(ray, tri) is None)

        # test for the line is on the vertex of the triangle.
        ray = Vector(Point3D(0, 0, 0), Point3D(1, 0, 0))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(line_in_triangle(ray, tri) is None)

        # test: the line is outside the triangle.
        ray = Vector(Point3D(0, 0.3, -0.2), Point3D(1, 0.3, -0.2))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(line_in_triangle(ray, tri) is None)

        # test for the normal case
        ray = Vector(Point3D(0, 0.2, -0.3), Point3D(1, 0.2, -0.3))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(line_in_triangle(ray, tri) is not None)


    def test_ray_in_triangle(self):

        # test for the line is parallel to the plane.
        ray = Vector(Point3D(0, 0, 0), Point3D(1, 0, 0))
        tri = Triangle(Point3D(0, 0, 1),
                       Point3D(1, 0, 1),
                       Point3D(0, 1, 1))
        
        self.assertTrue(ray_in_triangle(ray, tri) is None)

        # test for the line is on the vertex of the triangle.
        ray = Vector(Point3D(0, 0, 0), Point3D(1, 0, 0))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(ray_in_triangle(ray, tri) is None)

        # test: the line is outside the triangle.
        ray = Vector(Point3D(0, 0.3, -0.2), Point3D(1, 0.3, -0.2))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(ray_in_triangle(ray, tri) is None)

        # test: ray points outwards from the triangle.
        ray = Vector(Point3D(1, 0.2, -0.3), Point3D(0, 0.2, -0.3))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(ray_in_triangle(ray, tri) is None)

        # test: ray points outwards from the triangle.
        ray = Vector(Point3D(1, 0.2, -0.3), Point3D(0, 0.2, -0.3))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(ray_in_triangle(ray, tri, include_start_point=True) is not None)

        # test: ray points outwards from the triangle.
        ray = Vector(Point3D(0.9, 0.2, -0.3), Point3D(0, 0.2, -0.3))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(ray_in_triangle(ray, tri, include_start_point=True) is None)

        # test for the normal case
        ray = Vector(Point3D(0, 0.2, -0.3), Point3D(1, 0.2, -0.3))
        tri = Triangle(Point3D(1, 0, 0),
                       Point3D(1, 0, -1),
                       Point3D(1, 1, -1))
        
        self.assertTrue(ray_in_triangle(ray, tri) is not None)
