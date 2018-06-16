from relaxrender.LoopSubdivision import *

def test_LoopSubdivison():
    vertices = [[10,10,10],[-100,10,-10],[-100,-10,10],[10,-10,-10]] 
    faces = [[0,1,2],[0,2,3],[0,3,1],[3,2,1]]
    return loop(vertices,faces)

(vertices,faces)=test_LoopSubdivison()
print(vertices,faces)