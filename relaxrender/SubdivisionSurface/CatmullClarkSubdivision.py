'''
    TODO: finish Catmull Clark Subdivision
'''

from relaxrender.triangle import Triangle,Triangles
from relaxrender.points import Point,Point3D


from mpl_toolkits.mplot3d import Axes3D  
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
import matplotlib.pyplot as plt
import numpy as np

#__all__==['CatmullClarkSubdivision']

def  CatmullClarkSubdivision(faces,num):
    lines=[]
    points=[]
    face_to_lines={}
    line_to_points={}
    point_to_lines={}
    line_to_faces={}
    
    for i in range(num):
        lines,line_to_faces,face_to_lines=build_index(faces)
        print(line_to_faces,face_to_lines)
        points,point_to_lines,line_to_points=build_index(lines)
        draw(face_to_lines,line_to_points,points)
        faces=CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)


def draw(face_to_lines,line_to_points,points):
    verts=list((p.data[0],p.data[1],p.data[2]) for p in points)
    faces=[]
    print(face_to_lines,line_to_points)
    for ftl in face_to_lines.values():
        faces.append([])
        faces[-1].extend(line_to_points[ftl[0]])
        tmp=[ftl[0]]
        for i in range(2):
            for ltp in ftl:
                print(ftl,ltp)
                if ltp not in tmp and faces[-1][-1] in line_to_points[ltp]:
                    faces[-1].append(np.abs(1-line_to_points[ltp].index(faces[-1][-1])))
                    tmp.append(ltp)
                    
        

    poly3d = [[verts[vert_id] for vert_id in face] for face in faces]  
    # print(poly3d)  
    fig = plt.figure()  
    ax = fig.gca(projection='3d')
    # 绘制顶点  
    x, y, z = zip(*verts)  
    ax.scatter(x, y, z)  
    # 绘制多边形面  
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors='w', linewidths=1, alpha=0.3))  
    # 绘制对变形的边  
    ax.add_collection3d(Line3DCollection(poly3d, colors='k', linewidths=0.5, linestyles=':'))  
    
     # 设置图形坐标范围  
    ax.set_xlabel('X')  
    ax.set_xlim3d(-0.5, 1.5)  
    ax.set_ylabel('Y')  
    ax.set_ylim3d(-0.5, 1.5)  
    ax.set_zlabel('Z')  
    ax.set_zlim3d(-0.5, 1.5)  
    plt.show()


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
        point: Point
    return:
        [points,faces]

    PS：this func is not designed as a interface
'''
def CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines):
    face_points=[]
    for face in faces:
        temp=[]
        for l in face:
            temp.append(l[0].data)
            temp.append(l[1].data)
        data=sum(temp)/2/len(face)
        face_points.append(Point(p=Point3D.create(data)))
    edge_points=[]
    
    for i in len(lines):
        temp=[]
        temp.append(face_points[line_to_faces[i][0]].data)
        temp.append(face_points[line_to_faces[i][1]].data)
        temp.append(points[line_to_points[i][0]].data)
        temp.append(points[line_to_points[i][1]].data)
        data=sum(temp)/4
        edge_points.append(Point(p=Point3D.create(data)))
    vertes_points=[]
    for i in range(len(points)):
        data1=np.array([0,0])
        data2=np.array([0,0])
        for j in point_to_lines[i]:
            data1+=(lines[j][0].data+lines[j][1].data)/2
            data2+=(face_points[line_to_faces[j][0]].data+face_points[line_to_faces[j][1]].data)/2
        points[i].data=(data2+2*data1+(len(point_to_lines[i])-3)*points[i].data)/len(point_to_lines[i])
    re_faces=[]
    for i in range(len(face_points)):
        tmp=[]
        for j in face_to_lines[i]:
            for k in line_to_points[j]:
                if k not in  tmp:
                    re_faces.append([face_points[i],points[k]])
                    re_faces[-1].extend(list(edge_points[p_i] for p_i in point_to_lines[k] and face_to_lines[i] ))
                    tmp.append(j)
    return re_faces


if __name__=='__main__':
    verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
    points=list(Point.create(np.array(list(v))) for v in verts)
    line_to = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]
    face_to = [[0,1,2,3],[4,5,6,7],[0,4,8,9],[1,5,9,10],[2,6,10,11],[3,7,11,8]]  
    lines=[]
    for lt in line_to:
        lines.append([])
        for i in lt:
            lines[-1].append(points[i])
    faces=[]
    for ft in face_to:
        faces.append([])
        for i in ft:
            faces[-1].append(lines[i])
    CatmullClarkSubdivision(faces,1)


