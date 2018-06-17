import numpy as np
from .points import Point3D, Point

# points_doos=list()
# points_current=list()

'''
one point for another ones on the faces beside it
'''
# points_doos={}
current_points = []
current_faces = []
points_doos = []


class Face:
    def __init__(self, points):
        self.points = points


"""
    DOO_Sabin(faces,times):
    input:faces(list) , subdivision times
    output:new faces(list)



    faces :list of face
    face  : points : list of point
"""

def DOO_Sabin(faces,times):
    new_faces=[]
    for f in faces:
        n_f=Face(f)
        new_faces.append(n_f)
    for i in range(0,times):
        _DOO_Sabin_single_time(new_faces)
    return new_faces


# class points_doo:
#     def __init__(self,main_point,points):
#         self.main_point=main_point
#         self.points=points
#     def add_point(self,p):
#         self.points.append(p)


def _change_faces(x_faces):
    s_faces=[]
    for f in x_faces:
        new_points=[]
        for l in f:
            new_points.append(l[0])
            new_points.append(l[1])
        new_f=new_points
        s_faces.append(new_f)
    return s_faces



def _DOO_Sabin_single_time(faces):
    for f in faces:
        f = _get_new_face(f)
    for points_ds in points_doos:
        new_face = Face(points_ds)
        faces.append(new_face)
    return faces


def _get_face_point(face):
    face_point = _get_average_point(face.points)
    return face_point


'''
for each point in a face, there would be a new point
'''


def _get_new_face(face):
    face_point = _get_face_point(face)
    new_face_points = []
    for p in face.points:

        '''
        _______global variables_______
         '''
        if p not in current_points:
            current_points.append(p)
            flag = True
        else:
            flag=False

        if face.points.index(p) == 0:
            tmp1 = len(face.points) - 1
            tmp2 = face.points.index(p) + 1

        elif face.points.index(p) == len(face.points) - 1:
            tmp1 = face.points.index(p) - 1
            tmp2 = 0
        else:
            tmp1 = face.points.index(p) - 1
            tmp2 = face.points.index(p) + 1

        last_average_line = _get_average_point([p, face.points[tmp1]])
        next_average_line = _get_average_point([p, face.points[tmp2]])

        new_face_point = _get_average_point([p, face_point, last_average_line, next_average_line])

        new_face_points.append(new_face_point)

        # '''
        # append p's points
        # '''
        # if points_doos.has_key(p):
        #     p_points = points_doos[p]
        #     p_points.append(new_face_point)
        #     '''
        #     _______global variables_______
        #     '''
        #     points_doos[p] = p_points
        # else:
        #     p_points=[new_face_point,]
        #     p_points.append(new_face_point)
        #     '''
        #     _______global variables_______
        #     '''
        #     points_doos[p]=p_points
        if flag:
            points_doos.append([new_face_point, ])
        else:
            points_doos[current_points.index(p)].append(new_face_point)

    face.points = new_face_points
    new_face=Face(new_face_points)
    return new_face


def _get_average_point(points):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for p in points:
        x_sum = x_sum + p.data[0]
        y_sum = y_sum + p.data[1]
        z_sum = z_sum + p.data[2]
    Apoint = Point3D(x_sum / len(points), y_sum / len(points), z_sum / len(points))
    return Apoint


'''
debug:print the x,y,z of the point
'''


def _print_point(p):
    tmp = [p.data[0], p.data[1], p.data[2]]
    print(tmp)


'''
debug:print the points of the face
'''
def _print_face(f):
    for p in f.points:
        _print_point(p)


'''
debug:print the points
'''
def _print_points(ps):
    for p in ps:
        _print_point(p)



'''
debug:print the faces of the object
'''
def print_obj(faces):
    i=0
    for f in faces:
        i=i+1
        print("face",i)
        _print_face(f)


def _change_point(point,color):
    new_point=Point(point)
    new_point.color=color
    return new_point



"""
test:
input: cube's faces,6 times
output:new faces
"""
# if __name__ == '__main__':
#     point_test_1 = Point3D(4, 4, 4)
#     point_test_2 = Point3D(4, 4,0)
#     point_test_3 = Point3D(4, 0, 4)
#     point_test_4 = Point3D(4, 0, 0)
#     point_test_5 = Point3D(0, 4, 4)
#     point_test_6 = Point3D(0, 4, 0)
#     point_test_7 = Point3D(0, 0, 4)
#     point_test_8 = Point3D(0, 0, 0)
#     face_test_1 = Face([point_test_1, point_test_2, point_test_3, point_test_4])
#     face_test_2 = Face([point_test_1, point_test_5, point_test_6, point_test_2])
#     face_test_3 = Face([point_test_1, point_test_5, point_test_7, point_test_3])
#     face_test_4 = Face([point_test_3, point_test_4, point_test_8, point_test_7])
#     face_test_5 = Face([point_test_5, point_test_6, point_test_8, point_test_7])
#     face_test_6 = Face([point_test_2, point_test_4, point_test_8, point_test_6])
#     faces_test=[face_test_1,face_test_2,face_test_3,face_test_4,face_test_5,face_test_6]
#     _print_obj(DOO_Sabin(faces_test,6))
#     # points_test=[point_test_1,point_test_2,point_test_3,point_test_4]
#     # face_test=Face(points_test)
#     # _print_face(_get_new_face(face_test))
#     # for ps in points_doos:
#     #     _print_points(ps)
#
