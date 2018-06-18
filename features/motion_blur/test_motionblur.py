from matplotlib import pyplot as plt
# from features.motion_blur.motionblur import linear_motion_blur
from motionblur import linear_motion_blur
import imageio
import numpy as np
import unittest
import math


class TestMotionBlur(unittest.TestCase):
    #  测试对象的初始化工作
    def setUp(self):
        self.img = imageio.imread('./picture_test.jpg')  # shape of img is (682,1023,3)
        self.area = (40, 681, 217, 766)
        self.linear_motion_blur = linear_motion_blur
        self.dim = 10
        self.angle = 45
        self.filename = 'picture_test_blur.jpg'
        self.kernelCenter = int(math.floor(self.dim / 2))

    def test_LinearMotionBlur_random(self):
        self.linear_motion_blur.LinearMotionBlur_random(self.img)

    def test_LinearMotionBlur(self):
        self.linear_motion_blur.LinearMotionBlur(self.img, dim=self.dim, angle=self.angle, area=self.area,
                                                 filename=self.filename)

    def test_LineKernel(self):
        self.linear_motion_blur.LineKernel(dim=self.dim, angle=self.angle)

    def test_sanitize_angleValue(self):
        self.linear_motion_blur.sanitize_angleValue(kernelCenter=self.kernelCenter, angle=self.angle)

    def test_nearestValue(self):
        self.linear_motion_blur.nearestValue(theta=np.random.randint(0, 180, 1),
                                             validAngles=np.linspace(0, 180, 4, endpoint=False))

    def test_randomAngle(self):
        self.linear_motion_blur.randomAngle(kerneldim=self.dim)


def runTest():
    if __name__ == "__main__":
        unittest.main()


runTest()

# img = imageio.imread('./picture_test.jpg')  # shape of img is (682,1023,3)
# area = (40, 681, 217, 766)
# # img_origin = linear_motion_blur.LinearMotionBlur_random(img)
# img_blur = linear_motion_blur.LinearMotionBlur(img, dim=20, angle=135, area=area, filename='picture_test_blur.jpg')
# # img_blur_withoutarea = linear_motion_blur.LinearMotionBlur(img, dim=20, angle=135)
# plt.figure("img_blur")  # 图像窗口名称
# # plt.imshow(img_origin)
# plt.imshow(img_blur)
# plt.axis('on')  # 开启坐标轴
# plt.title('img_blur')  # 图像题目
# plt.show()
