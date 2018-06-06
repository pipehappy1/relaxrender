'''
    TODO: finish Catmull Clark Subdivision
        data struct:
            point: relaxrender.points.Point3D
            line : relaxrender.points.Vector
            face : [line,line,...]
'''

from relaxrender.points import Point3D,Vector
import numpy as np

__all__==['CatmullClarkSubdivision']

'''
    subdivide a model according to its points and faces
    return points and faces after subdivision

    param:
        points: [point,point,...]
        faces : [face,face,...]
    return:
        [points,faces]
'''
def CatmullClarkSubdivision(points,faces):

    pass




