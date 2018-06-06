import numpy as np
from .points import Point3D, Point, Vector, Points, Point3D_store

class Triangle:
    data_width = Point.data_width*3 + Vector.data_width
    
    def __init__(self, p1, p2, p3, n=Vector.place_holder()):
        # p1, p2, p3 are Point3D type of object.
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        if n.is_place_holder():
            pv1 = self.p2 - self.p1
            pv2 = self.p3 - self.p1
            tnorm = np.cross(pv1.data, pv2.data)
            if np.linalg.norm(tnorm) < 1e-6:
                raise ValueError('bad norm.')
            tnorm = tnorm / np.linalg.norm(tnorm)
            self.norm = Vector(Point3D(0, 0, 0),
                               Point3D(tnorm[0],
                                       tnorm[1],
                                       tnorm[2]))
        else:
            self.norm = n

    def verify(self):
        tv1 = self.p2 - self.p1
        tv2 = self.p3 - self.p1
        tnorm = np.cross(tv1.data, tv2.data)
        tnorm = tnorm / np.linalg.norm(tnorm)
        tnorm1 = self.norm.end - self.norm.start
        tnorm1 = tnorm1.data / np.linalg.norm(tnorm1.data)
        return np.sum(np.abs((tnorm - tnorm1).data)) < 1e-6

    def __eq__(self, other):
        return np.max((np.linalg.norm(self.p1.data-other.p1.data),
                       np.linalg.norm(self.p2.data-other.p2.data),
                       np.linalg.norm(self.p3.data-other.p3.data))) < 1e-6

        

class Triangles:
    chunk_size = 128
    data_width = None
    
    def __init__(self, src=None, copy=False):
        if src is not None and copy == True:
            self.points = src.points.copy()
            self.triangles = src.triangles.copy()
            self.memory_size = src.memory_size
            self.cindex = src.cindex
        else:
            self.points = Point3D_store()
            self.triangles = np.empty((Triangles.chunk_size, 3 + Vector.data_width))
            self.memory_size = Triangles.chunk_size
            self.cindex = 0

    def size(self):
        return self.cindex

    def items(self):
        raise NotImplementedError

    def __getitem__(self, key):
        p1_index = int(self.triangles[key, 0])
        p2_index = int(self.triangles[key, 1])
        p3_index = int(self.triangles[key, 2])

        p1 = self.points[p1_index]
        p2 = self.points[p2_index]
        p3 = self.points[p3_index]

        vnorm = Vector(Point3D.create(self.triangles[key, 3:6]),
                       Point3D.create(self.triangles[key, 6:9]))

        return Triangle(p1, p2, p3, vnorm)

    def append_tri(self, a1, a2, a3):
        # The inputs are 3 numpy array for 3 points.
        self.add_triangle(Triangle(Point3D.create(a1),
                                   Point3D.create(a2),
                                   Point3D.create(a3)))
        return self
        

    def append_rct(self, a1, a2, a3, a4):
        # The inputs are 4 numpy array for 4 points for a rectangle.
        self.add_triangle(Triangle(Point3D.create(a1),
                                   Point3D.create(a2),
                                   Point3D.create(a3)))
        self.add_triangle(Triangle(Point3D.create(a1),
                                   Point3D.create(a3),
                                   Point3D.create(a4)))
        return self

    def add_triangle(self, tri):
        self.points.add_point(tri.p1)
        self.points.add_point(tri.p2)
        self.points.add_point(tri.p3)
        self.triangles[self.cindex, 0] = self.points.cindex -3
        self.triangles[self.cindex, 1] = self.points.cindex -2
        self.triangles[self.cindex, 2] = self.points.cindex -1
        self.triangles[self.cindex, 3:6] = tri.norm.start.data
        self.triangles[self.cindex, 6:9] = tri.norm.end.data
        self.triangles[self.cindex, 9] = Vector.mode[tri.norm.mode]

        self.cindex += 1

        if self.memory_size == self.cindex:
            self.data = concatenate((self.data,
                                     np.empty((Points.chunk_size, Points.data_width))),
                                    axis=0)
            self.memory_size += Triangles.chunk_size
        
        return self

    @classmethod
    def add_triangles(cls, triangles_list):
        pass

    def __str__(self):
        ret = ""
        for i in range(self.size()):
            ret += "triangle: {}\n".format(i)
            ret += self.points[int(self.triangles[i,0])].data.__str__() + "\n"
            ret += self.points[int(self.triangles[i,1])].data.__str__() + "\n"
            ret += self.points[int(self.triangles[i,2])].data.__str__() + "\n"
        return ret

    def copy(self):
        ret = Triangles(src=self, copy=True)
        return ret
        
