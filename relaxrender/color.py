import numpy as np

class Color:
    supported_color_space = {'RGB':0.0,
                             'RGBA':1.0,
                             'place_holder':100.0}

    data_width = 5
    
    def __init__(self, mode, v1, v2, v3, v4):
        if mode in Color.supported_color_space:
            self.mode = mode
        else:
            raise ValueError('unsupported color space!')

        self.color = np.array([0.0, 0.0, 0.0, 0.0])
        self.color[0] = v1
        self.color[1] = v2
        self.color[2] = v3
        self.color[3] = v4

    def __mul__(self, o):
        ret = Color('RGB', 1, 1, 1, 1)
        if self.mode == o.mode:
            ret.color = self.color * o.color
        else:
            raise ValueError

        return ret

    @classmethod
    def place_holder(cls):
        return cls('place_holder', 0.0, 0.0, 0.0, 0.0)

White = Color('RGB', 1, 1, 1, -1)
Black = Color('RGB', 0, 0, 0, -1)
Red = Color('RGB', 1, 0, 0, -1)
Green = Color('RGB', 0, 1, 0, -1)
Blue = Color('RGB', 0, 0, 1, -1)
Grey = Color('RGB', 0.5, 0.5, 0.5, -1)

