
from .mesh import *
from .camera import *

__all__ = ['Scene']

class Scene:
    def __init__(self, mesh, camera):
        self.mesh = mesh
        self.camera = camera

