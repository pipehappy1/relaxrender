"""
    this module include function to draw,which is used during test
    this module is also used to test CatmullClarkSubdivison 
"""
import unittest
from mpl_toolkits.mplot3d import Axes3D  
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
import matplotlib.pyplot as plt
import numpy as np
from relaxrender.points import Point,Point3D
from relaxrender.CatmullClarkSubdivision import _CatmullClarkSubdivision_in,_build_index

__author__="X-wenhao"


class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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


class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
    
    class TestCatmullClarkSubdivision(unittest.TestCase):


    def test_CatmullClarkSubdivision(self):
        
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
        
        lines,line_to_faces,face_to_lines=_build_index(faces)
        points,point_to_lines,line_to_points=_build_index(lines)

        for i in range(4):
            lines,line_to_faces,face_to_lines=_build_index(faces)
            #print(line_to_faces,face_to_lines)
            points,point_to_lines,line_to_points=_build_index(lines)
            #draw(face_to_lines,line_to_points,points)
            self.assertTrue(_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines))
            faces=_CatmullClarkSubdivision_in(faces,lines,points,face_to_lines,line_to_points,line_to_faces,point_to_lines)
            print('subdividing {},and there are {} faces now'.format(i+1,len(faces)))

        
        

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
