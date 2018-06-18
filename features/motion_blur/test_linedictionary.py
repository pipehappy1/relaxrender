# from features.motion_blur.motionblur.LineDictionary import LineDictionary
from motionblur.LineDictionary import LineDictionary
import unittest


class TestLineDictionary(unittest.TestCase):
    #  测试对象的初始化工作
    def setUp(self):
        self.dim = 10
        self.angle = [0, 45, 90, 135]
        self.LineDictionary = LineDictionary()

    def test_create_kernel(self):
        self.LineDictionary.create_kernel(dim=self.dim, angle=self.angle[0])
        self.LineDictionary.create_kernel(dim=self.dim, angle=self.angle[1])
        self.LineDictionary.create_kernel(dim=self.dim, angle=self.angle[2])
        self.LineDictionary.create_kernel(dim=self.dim, angle=self.angle[3])


def runTest():
    if __name__ == "__main__":
        unittest.main()


runTest()
