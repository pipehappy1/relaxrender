'''
    TODO: finish Catmull Clark Subdivision
'''

from relaxrender.triangle import Triangle,Triangles
from relaxrender.points import Point3D,Vector
import numpy as np

__all__==['CatmullClarkSubdivision']

def  CatmullClarkSubdivision(faces):
    lines=[]
    points=[]
    face_to_lines={}
    line_to_points={}
    point_to_lines={}
    line_to_faces={}
    lines,line_to_faces,face_to_lines=build_index(faces)
    points,point_to_lines,line_to_points=build_index(lines)
    
    return lines,line_to_faces,face_to_lines

def build_index(faces):
    lines=[]
    face_to_lines={}
    line_to_faces={}
    for face_i in range(len(faces)):
        face=faces[face_i]
        face_to_lines[face_i]=[]
        for line_i in range(len(faces[face_i])):
            line=face[line_i]
            if  line not in lines:
                lines.append(line)
                line_to_faces[len(lines)-1]=[]
            face_to_lines[face_i].append(lines.index(line))
            line_to_faces[lines.index(line)].append(face_i)
    return lines,line_to_faces,face_to_lines   

'''
    subdivide a model according to its points and faces
    return points and faces after subdivision

    param:
        faces : [face,face,...]
        face:   [line,line,...]
        line:   [point,point]
        point: Point3D
    return:
        [points,faces]

    PS：this func is not designed as a interface
'''
def CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines):
    face_points=list(map((lambda face: sum(list(l[0] for l in face)+list(l[1] for l in face))/2.0/len(face) ,faces)))
    edge_points=list( (face_points[line_to_faces[i][0]]+face_points[line_to_faces[i][1]]+points[line_to_points[i][0]]+points[line_to_points[i][1]])/4.0 for i in len(lines))


def getFacePoint(face):
    x=1.0/2/len(face)*(sum(list(l.p_start for l in face)))



