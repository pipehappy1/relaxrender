

from relaxrender.points import Point3D, Point2D
from relaxrender.triangle import Triangle, Triangles
from relaxrender.mesh import Mesh
from relaxrender.texture import PlaneLightSource, BlackSink, ReflectionSurface, GlassSurface, SemiTransparent

__all__ = ['CenterSquareLight']

class SolidCube(Mesh):
    def __init__(self, center=Point3D.origin(), half_size=0.25):
        super().__init__()
        self.center = center
        self.half_size = half_size

    

class CenterSquareLight(Mesh):
    def __init__(self):
        tris = Triangles()
        tris.add_triangle(Triangle(Point3D(0, 0, 0),
                                   Point3D(1, 0, 0),
                                   Point3D(0, 1, 0)))
        tris.add_triangle(Triangle(Point3D(0, 1, 0),
                                   Point3D(1, 0, 0),
                                   Point3D(1, 1, 0)))

        texs = [PlaneLightSource(), PlaneLightSource()]

        tex_pos = [None, None]
        
        super().__init__(tris, texs, tex_pos)
