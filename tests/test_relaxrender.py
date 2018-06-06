import unittest

import relaxrender.points as rp
import relaxrender.color as color
import relaxrender.mesh as mesh
import relaxrender.example_scene as example
import relaxrender.raycasting as raycasting
import relaxrender.context as ctx
import relaxrender.screenwriter as sw

class TestRelaxRender(unittest.TestCase):

    def test_simple_render(self):
        
        scene = example.cornell_box

        render = raycasting.SimpleReverseRayCasting(ctx.Context())
        input_xy, output_color = render.drive_raycasting(scene)
        
        writer = sw.NormalizedWriter(ctx.Context())
        writer.write(input_xy, output_color, 'output_test.jpg')

        
