import unittest
from entrance import ray_tracing

class TestStochaticRayTracing(unittest.TestCase):
    def test_main(self):
        #执行随机光线追踪渲染
        ray_tracing()