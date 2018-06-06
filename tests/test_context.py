import unittest

import relaxrender.context as ctx

class TestContext(unittest.TestCase):

    def test_ctx(self):
        c = ctx.Context()
        c.color_mode = 'unknown_mode'
        with self.assertRaises(ValueError):
            c.integration_test()

        c = ctx.Context()
        c.writer_output_device = 'unknown_device_type'
        with self.assertRaises(ValueError):
            c.integration_test()

        c = ctx.Context()
        c.writer_color_mode = 'unknown_mode'
        with self.assertRaises(ValueError):
            c.integration_test()
        
        
