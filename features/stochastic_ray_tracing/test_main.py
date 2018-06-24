import unittest
import entrance

class TestStochaticRayTracing(unittest.TestCase):
    def test_main(self):
        #执行随机光线追踪渲染
        entrance.ray_tracing()