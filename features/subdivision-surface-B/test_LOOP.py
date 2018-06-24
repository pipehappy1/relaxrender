import unittest
from LOOP import *


'''
    input:vertices=[[x0,y0,z0],[x1,y1,z1]...],faces=[[index0,index1,index2]...]
    output:new_vertices,new_face
'''
class TestLoopSubdivison(unittest.TestCase):

    def test_LoopSubdivison(self):
        vertices = [[10,10,10],[-100,10,-10],[-100,-10,10],[10,-10,-10]] 
        faces = [[0,1,2],[0,2,3],[0,3,1],[3,2,1]]
        loop(vertices,faces)
