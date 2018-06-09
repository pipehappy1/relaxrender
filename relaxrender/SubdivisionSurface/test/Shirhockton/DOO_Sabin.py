import numpy as np
from relaxrender.points import Point3D,Point

# points_doos=list()
# points_current=list()


class face:
    def __init__(self, points):
        self.points=points
# class points_doo:
#     def __init__(self,main_point,points):
#         self.main_point=main_point
#         self.points=points
#     def add_point(self,p):
#         self.points.append(p)

def DOO_Sabin(faces):
    for f in faces:
        f=get_new_face(f)
    return faces

def get_face_point(face):
    face_point=get_average_point(face.points)
    return face_point

def get_new_face(face):
    face_point=get_face_point(face)
    new_face_points=list()
    for p in face.points:

        if face.points.index(p)==0:
            tmp1=len(face.points)-1
            tmp2=face.points.index(p)+1

        elif face.points.index(p)==len(face.points)-1:
            tmp1=face.points.index(p)-1
            tmp2=0
        else:
            tmp1=face.points.index(p)-1
            tmp2=face.points.index(p)+1

        last_average_line=get_average_point([p,face.points[tmp1]])
        next_average_line=get_average_point([p,face.points[tmp2]])

        new_face_point=get_average_point([p,face_point,last_average_line,next_average_line])

        new_face_points.append(new_face_point)

    face.points=new_face_points

    return new_face_points

def get_average_point(points):
    x_sum=0
    y_sum=0
    z_sum=0
    for p in points:
        x_sum=x_sum+p.x
        y_sum=y_sum+p.y
        z_sum=z_sum+p.z
    Apoint=Point(x_sum/3,y_sum/3,z_sum/3)
    return Apoint
