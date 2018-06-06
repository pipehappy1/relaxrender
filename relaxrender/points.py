import numpy as np

from .color import Color

__all__ = ['Point3D', 'Point2D', 'Vector', 'Point', 'Point3D_store', 'Points']

class Point3D:
    data_width = 3
    def __init__(self, x, y, z):
        self.data = np.array([0.0, 0.0, 0.0])
        self.data[0] = x
        self.data[1] = y
        self.data[2] = z

    @classmethod
    def create(cls, data):
        p = Point3D(0, 0, 0)
        p.data = data
        return p

    @classmethod
    def origin(cls):
        return Point3D(0, 0, 0)

    def __sub__(self, other):
        p = Point3D(self.data[0]-other.data[0],
                    self.data[1]-other.data[1],
                    self.data[2]-other.data[2])
        return p

    def __eq__(self, other):
        return self.data[0] == other.data[0] and self.data[1] == other.data[1] and self.data[2] == other.data[2]

class Point2D:
    def __init__(self, x, y):
        self.data = np.array([0.0, 0.0])
        self.data[0] = x
        self.data[1] = y

    @classmethod
    def origin(self):
        return Point2D(0, 0)

class Vector:
    mode = {'real':0.0,
            'place_holder':100.0}
    data_width = Point3D.data_width*2 + 1
    
    def __init__(self, p_start, p_end):
        # p_start and p_end is point3D.
        # for line, p_start and p_end are two points on the line.
        # for ray, p_start is the starting point, p_end is some point on the ray.
        # for segment, p_start is one end point, p_end is the other end point.
        self.start = p_start
        self.end = p_end
        self.mode = 'real'

    @classmethod
    def place_holder(cls):
        res = cls(Point3D(0.0, 0.0, 0.0),
                  Point3D(0.0, 0.0, 0.0))
        res.mode = 'place_holder'
        return res

    def is_place_holder(self):
        return self.mode == 'place_holder'

class Point(Point3D):
    data_width = Point3D.data_width + Color.data_width + Vector.data_width
    
    def __init__(self, x=None, y=None, z=None, p=None, c=None, n=None):
        # either x, y, z are given or p is given.
        if x is None and y is None and z is None and p is None:
            raise ValueError('needs either x,y,z or 3dpoint.')
        else:
            if x is None or y is None or z is None:
                super().__init__(p.data[0],
                                 p.data[1],
                                 p.data[2])
            else:
                super().__init__(x, y, z)

        self.color = c
        self.norm = n


class Point3D_store:
    chunk_size = 128
    data_width = Point3D.data_width
    
    def __init__(self, src=None, copy=False):
        if src is not None and copy == True:
            self.data = np.array(src.data, copy=True)
            self.size = src.size
            self.cindex = src.cindex
        else:
            self.data = np.empty((Point3D_store.chunk_size, Point3D.data_width))
            self.size = Point3D_store.chunk_size
            self.cindex = 0


    def __getitem__(self, key):
        return Point3D(self.data[key, 0],
                       self.data[key, 1],
                       self.data[key, 2])

    def size(self):
        return self.cindex

    def add_point(self, p):
        self.data[self.cindex, :] = p.data
        self.cindex += 1

        if self.size == self.cindex:
            self.data = np.concatenate((self.data,
                                        np.empty((Points.chunk_size, Points.data_width))),
                                       axis=0)
            self.size += Points.chunk_size
        
    @classmethod
    def add_points(cls, ps_list):
        raise NotImplementedError

    def copy(self):
        ret = Point3D_store(src=self, copy=True)
        return ret

class Points:
    chunk_size = 128
    # 3 for xyz, 3 for norm start, 3 for norm end,
    # 4 for color, 1 for norm mode, 1 for color mode
    data_width = Point.data_width
    
    def __init__(self):
        self.data = np.empty((Points.chunk_size, Points.data_width)) 
        self.size = Points.chunk_size
        self.cindex = 0

    def __getitem__(self, key):
        raise NotImplementedError

    def get_point3d(self, key):
        raise NotImplementedError
        
    def add_point(self, p):
        self.data[self.cindex, 0:3] = p.data
        self.data[self.cindex, 3:6] = p.norm.start.data
        self.data[self.cindex, 6:9] = p.norm.end.data
        self.data[self.cindex, 9:13] = p.color.color
        self.data[self.cindex, 13] = Vector.mode[p.norm.mode]
        self.data[self.cindex, 14] = Color.supported_color_space[p.color.mode]

        self.cindex += 1

        if self.size == self.cindex:
            self.data = np.concatenate((self.data,
                                        np.empty((Points.chunk_size, Points.data_width))),
                                       axis=0)
            self.size += Points.chunk_size

    @classmethod
    def add_points(cls, ps_list):
        pass
