'''
    TODO: finish Catmull Clark Subdivision
'''

from relaxrender.triangle import Triangle,Triangles
from relaxrender.points import Point,Point3D
import numpy as np
#__all__==['CatmullClarkSubdivision']

'''
    接口函数
    param：
        faces : [face,face,...]
        face:   [line,line,...]
        line:   [point,point]
        point: Point
        num：how many times you want to subdivide
'''
def  CatmullClarkSubdivision(faces,num):
    lines=[]
    points=[]
    face_to_lines={}
    line_to_points={}
    point_to_lines={}
    line_to_faces={}
    
    for i in range(num):
        lines,line_to_faces,face_to_lines=_build_index(faces)
        #print(line_to_faces,face_to_lines)
        points,point_to_lines,line_to_points=_build_index(lines)
        #draw(face_to_lines,line_to_points,points)
        #print("lines:",lines)
        faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
    return faces


def _build_index(faces):
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
        point: Point
    return:
        [points,faces]

    PS：this func is not designed as a interface
'''
def _CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines):
    #print("old_points:",list((p.data[0],p.data[1],p.data[2]) for p in points))
    #print("face_to_lines:",face_to_lines)
    #print("line_to_points:",line_to_points)
    #print("line_to_faces:",line_to_faces)
    #print("point_to_lines:",point_to_lines)
    face_points=[]
    for face in faces:
        temp=[]
        for l in face:
            temp.append(l[0].data)
            temp.append(l[1].data)
        data=sum(temp)/2/len(face)
        face_points.append(Point(p=Point3D.create(data)))
    #print("face_points:",len(face_points),list((p.data[0],p.data[1],p.data[2]) for p in face_points))

    edge_points=[]
    
    for i in range(len(lines)):
        temp=[]
        temp.append(face_points[line_to_faces[i][0]].data)
        temp.append(face_points[line_to_faces[i][1]].data)
        temp.append(points[line_to_points[i][0]].data)
        temp.append(points[line_to_points[i][1]].data)
        data=sum(temp)/4
        edge_points.append(Point(p=Point3D.create(data)))
    #print("edge_points:",list((p.data[0],p.data[1],p.data[2]) for p in edge_points))
    
    vertes_points=[]
    for i in range(len(points)):
        data1=np.array([0.0,0.0,0.0])
        data2=np.array([0.0,0.0,0.0])
        for j in point_to_lines[i]:
            data1+=(lines[j][0].data+lines[j][1].data)/2.0/len(point_to_lines[i])
            data2+=(face_points[line_to_faces[j][0]].data+face_points[line_to_faces[j][1]].data)/2/len(point_to_lines[i])
        points[i].data=(data2+2*data1+(len(point_to_lines[i])-3)*points[i].data)/len(point_to_lines[i])
    #print("new_points:",list((p.data[0],p.data[1],p.data[2]) for p in points))
    
    re_faces=[]
    for i in range(len(face_points)):
        tmp=[]
        for j in face_to_lines[i]:
            for k in line_to_points[j]:
                if k not in  tmp:
                    re_faces.append([])
                    #print(point_to_lines[k],face_to_lines[i])
                    eps=list(edge_points[p_i] for p_i in [m for m in point_to_lines[k] if m in face_to_lines[i]] )
                    #print(eps)
                    for ep in eps:
                        re_faces[-1].extend([ [face_points[i],ep],[points[k],ep] ])
                    tmp.append(k)
    #print(len(re_faces),'\n',re_faces[0])
    return re_faces




