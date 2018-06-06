import numpy as np

from .triangle import Triangle, Triangles
from .points import Point3D, Vector

__all__ = ['dist',
           'sphere_sampling',
           'line_in_triangle',
           'ray_in_triangle']


def dist(p3d1, p3d2):
    return np.linalg.norm(p3d1.data - p3d2.data)


def sphere_sampling(sample_size):
    # according to https://en.wikibooks.org/wiki/Mathematica/Uniform_Spherical_Distribution
    theta = np.random.random((sample_size, 1)) * np.pi * 2
    phi = np.arccos(np.sqrt(np.random.random((sample_size, 1)))) *2

    res = np.concatenate((np.sin(phi)*np.cos(theta),
                          np.sin(phi)*np.sin(theta),
                          np.cos(phi)), axis=1)

    if sample_size == 1:
        return res[0,0], res[0, 1], res[0, 2]
    else:
        return res



def line_in_triangle(ray, triangle):
    """
    input: ray is a vector
    input: triangle is a Triangle

    output: interact point or None.
    """

    vray = ray.end.data - ray.start.data
    vnorm = triangle.norm.end.data - triangle.norm.start.data
    if np.abs(np.dot(vray, vnorm)) < 1e-3:
        return None

    tray = triangle.p1.data - ray.start.data
    alpha = np.dot(tray, vnorm) / np.dot(vray, vnorm)
    
    ipoint = alpha * ray.end.data + (1-alpha) * ray.start.data

    v1 = triangle.p1.data - ipoint
    v2 = triangle.p2.data - ipoint
    v3 = triangle.p3.data - ipoint
    v1norm = np.linalg.norm(v1)
    v2norm = np.linalg.norm(v2)
    v3norm = np.linalg.norm(v3)

    if v1norm < 1e-6 or v2norm < 1e-6 or v3norm < 1e-6:
        return None
    
    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)
    v3 = v3 / np.linalg.norm(v3)

    d1 = np.arccos(np.dot(v1, v2))
    d2 = np.arccos(np.dot(v2, v3))
    d3 = np.arccos(np.dot(v3, v1))

    if np.abs(np.sum((d1, d2, d3)) - np.pi*2) < 1e-3:
        return Point3D(ipoint[0], ipoint[1], ipoint[2])
    else:
        return None


def ray_in_triangle(ray, triangle, include_start_point=False):
    """
    input: ray is a vector
    input: triangle is a Triangle

    output: interact point or None.
    """
    vray = ray.end.data - ray.start.data
    vnorm = triangle.norm.end.data - triangle.norm.start.data
    if np.abs(np.dot(vray, vnorm)) < 1e-3:
        return None

    tray = triangle.p1.data - ray.start.data

    alpha = np.dot(tray, vnorm) / np.dot(vray, vnorm)

    if include_start_point:
        if alpha < 0:
            return None
    else:
        if alpha <= 0:
            return None
    
    ipoint = alpha * ray.end.data + (1-alpha) * ray.start.data

    v1 = triangle.p1.data - ipoint
    v2 = triangle.p2.data - ipoint
    v3 = triangle.p3.data - ipoint
    v1norm = np.linalg.norm(v1)
    v2norm = np.linalg.norm(v2)
    v3norm = np.linalg.norm(v3)

    if v1norm < 1e-6 or v2norm < 1e-6 or v3norm < 1e-6:
        return None
    
    v1 = v1 / np.linalg.norm(v1)
    v2 = v2 / np.linalg.norm(v2)
    v3 = v3 / np.linalg.norm(v3)

    d1 = np.arccos(np.dot(v1, v2))
    d2 = np.arccos(np.dot(v2, v3))
    d3 = np.arccos(np.dot(v3, v1))

    if np.abs(np.sum((d1, d2, d3)) - np.pi*2) < 1e-3:
        return Point3D(ipoint[0], ipoint[1], ipoint[2])
    else:
        return None
