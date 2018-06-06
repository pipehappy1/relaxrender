#
# This is about vertex transformation before rendering.
#
import numpy as np

from .points import Point3D, Vector
from .triangle import Triangle, Triangles

__all__ = ['PerspectiveCamera', 'OrthogonalCamera']

class CameraBase:
    def __init__(self, pos=None, up=None, right=None):

        self.pos = np.empty((1,3))
        self.up = np.empty(3)
        self.right = np.empty(3)

        if pos is not None:
            self.pos[:,:] = pos
        if up is not None:
            self.up = up / np.linalg.norm(up)
        if right is not None:
            self.right = right / np.linalg.norm(right)

        if np.dot(self.up, self.right) > 1e-6:
            raise ValueError

        self.inward = np.cross(self.right, self.up)

        self.relocate_mat = np.transpose(
            np.stack((self.right,
                      self.up,
                      self.inward)))

    def relocate_world_by_camera(self, triangles):
        ret_triangles = Triangles(src=triangles, copy=True)
        n = ret_triangles.points.data.shape[0]
        ret_triangles.points.data -= np.dot(np.ones((n,1)), self.pos)
        ret_triangles.points.data = np.dot(ret_triangles.points.data, self.relocate_mat)
        return ret_triangles

    def sample_vector(self, size=1):
        """
        Return size of Vector starting from 
            origin and uniformly distributed over camera rectangle.
        Return x,y coordinate on the [-1, 1] sqaure.
        """
        raise NotImplementedError


class PerspectiveCamera(CameraBase):
    def __init__(self, pos, up, right, h_angle, v_angle):
        super().__init__(pos, up, right)

        self.h_angle = h_angle
        self.v_angle = v_angle

    def sample_vector(self, size=1):
        samples = []
        xy = []
        for i in range(size):
            input_x = np.random.random()*2 - 1
            input_y = np.random.random()*2 - 1

            real_x = np.tan(self.h_angle/2)*input_x
            real_y = np.tan(self.v_angle/2)*input_y

            start_vector = Vector(Point3D(0, 0, 0),
                                  Point3D(real_x, real_y, -1))
            samples.append(start_vector)
            xy.append((input_x, input_y))
        return samples, xy


class OrthogonalCamera(CameraBase):
    def __init__(self, pos, up, right, width, height):
        super().__init__(pos, up, right)

        self.width = width
        self.height = height
        
    def sample_vector(self, size=1):
        samples = []
        xy = []
        for i in range(size):
            input_x = np.random.random()*2 - 1
            input_y = np.random.random()*2 - 1
            
            real_x = self.width/2*input_x
            real_y = self.height/2*input_y
            
            start_vector = Vector(Point3D(real_x, real_y, 0),
                                  Point3D(real_x, real_y, -1))
            samples.append(start_vector)
            xy.append((input_x, input_y))
        return samples, xy
        
