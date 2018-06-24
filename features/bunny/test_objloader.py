import unittest
import features.bunny.objloader as ol


class TestObjLoader(unittest.TestCase):
    def test_OBJ(self):
        obj = ol.OBJ("d:/relaxrender-bgroup/features/bunny/", "bunny.obj", swapyz=True)
        obj.create_bbox()
        obj.create_gl_list()