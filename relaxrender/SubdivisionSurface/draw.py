from mpl_toolkits.mplot3d import Axes3D  
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
import matplotlib.pyplot as plt
import numpy as np
from relaxrender.points import Point,Point3D

def draw(face_to_lines,line_to_points,points):
    verts=list((p.data[0],p.data[1],p.data[2]) for p in points)
    faces=[]
    #print(face_to_lines,line_to_points)
    for ftl in face_to_lines.values():
        faces.append([])
        faces[-1].extend(line_to_points[ftl[0]])
        tmp=[ftl[0]]
        for i in range(2):
            for ltp in ftl:
                #print(ftl,ltp)
                if ltp not in tmp and faces[-1][-1] in line_to_points[ltp]:
                    faces[-1].append(line_to_points[ltp][1-line_to_points[ltp].index(faces[-1][-1])])
                    tmp.append(ltp)
    #print(verts,'\n',faces)         
        

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