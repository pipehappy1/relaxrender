
import numpy as np
from .points import Point, Vector, Points
from .triangle import Triangle, Triangles

class Raster:
    # for OpenGL alike forward rendering.
    def __init__(self, context):
        self.context = context

    def rasterize(self, triangles):
        pass


class SimpleRaster(Raster):
    def __init__(self, context):
        super().__init__(context)

    def rasterize(self, triangles):
        pass
