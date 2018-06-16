import numpy as np
import unittest
from relaxrender.points import Point3D, Point
from DOO-SABIN import *

"""
    point_test_*:   Point3D
    face_test_*:    list of point_test
    faces_test:     list of face_test
    
"""

"""
    DOO_Sabin(faces,times):
    input:faces(list) , subdivision times
    output:new faces(list)
    faces :list of face
    face  : points : list of point
"""
class TestDOOSabinSubdivision(unittest.TestCase):

    #test for cubes
    def test_DOOSabin_subdivision(self):
        point_test_1 = Point3D(4, 4, 4)
        point_test_2 = Point3D(4, 4, 0)
        point_test_3 = Point3D(4, 0, 4)
        point_test_4 = Point3D(4, 0, 0)
        point_test_5 = Point3D(0, 4, 4)
        point_test_6 = Point3D(0, 4, 0)
        point_test_7 = Point3D(0, 0, 4)
        point_test_8 = Point3D(0, 0, 0)
        face_test_1 = [point_test_1, point_test_2, point_test_3, point_test_4]
        face_test_2 = [point_test_1, point_test_5, point_test_6, point_test_2]
        face_test_3 = [point_test_1, point_test_5, point_test_7, point_test_3]
        face_test_4 = [point_test_3, point_test_4, point_test_8, point_test_7]
        face_test_5 = [point_test_5, point_test_6, point_test_8, point_test_7]
        face_test_6 = [point_test_2, point_test_4, point_test_8, point_test_6]
        faces_test = [face_test_1, face_test_2, face_test_3, face_test_4, face_test_5, face_test_6]
DOO_Sabin(faces_test, 6)
