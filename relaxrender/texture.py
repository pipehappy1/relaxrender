import numpy as np

from .color import Color, White, Black, Red

class Texture:
    def __init__(self, data=None, bsdf=None):
        self.data = data
        self.bsdf = None

    def num_layer(self):
        pass

    def damping_rate(self):
        pass

    def get_color(self, x, y, z=None):
        pass


class PlaneLightSource(Texture):
    def __init__(self, color=White):
        super().__init__(color, None)

    def num_layer(self):
        return 1

    def damping_rate(self):
        return 0

    def get_color(self, incoming_color,
                  incoming_plane_angle,
                  incoming_norm_angle,
                  outgoing_plane_angle,
                  outgoing_norm_angle,
                  x, y,
                  z=None):
        
        return self.data



class BlackSink(Texture):
    def __init__(self, data=None, bsdf=None):
        super().__init__(data, bsdf)


class ReflectionSurface(Texture):
    def __init__(self, data=None, bsdf=None):
        super().__init__(data, bsdf)


class UniformReflection(ReflectionSurface):
    def __init__(self, color=Red):
        super().__init__(color, None)

    def num_layer(self):
        return 1

    def damping_rate(self):
        return 0.5

    def get_color(self, incoming_color,
                  incoming_plane_angle,
                  incoming_norm_angle,
                  outgoing_plane_angle,
                  outgoing_norm_angle,
                  x, y,
                  z=None):
        
        if incoming_color is None:
            return None
        else:
            return self.data * incoming_color


class GlassSurface(Texture):
    def __init__(self, data=None, bsdf=None):
        super().__init__(data, bsdf)


class SemiTransparent(Texture):
    def __init__(self, data=None, bsdf=None):
        super().__init__(data, bsdf)
