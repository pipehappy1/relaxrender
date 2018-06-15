import numpy as np

from .color import Color

class Context:
    output_device = ['jpg', 'mp4', 'screen']
    
    def __init__(self):
        self.color_mode = 'RGB'

        self.triangle_right_hand_norm = True
        
        self.x_right_from_screen = True
        self.y_up_from_screen = True
        self.z_face_screen = True

        self.x_range = (-1.0, 1.0)
        self.y_range = (-1.0, 1.0)
        self.z_range = (-1.0, 1.0)

        self.raycasting_iteration = int(1e6)

        self.writer_output_device = 'jpg'
        self.writer_color_mode = 'RGB'
        self.output_height = 600
        self.output_width = 800

    def integration_test(self):
        if self.color_mode not in Color.supported_color_space.keys():
            raise ValueError('unsupported color mode in context.')

        if self.writer_output_device not in Context.output_device:
            raise ValueError('unsupported output device.')

        if self.writer_color_mode not in Color.supported_color_space.keys():
            raise ValueError('unsupported writer color mode in context.')
