import unittest
from features.spatialDenoising.clear_noise import ClearNoise
class TestSpatialDenoising(unittest.TestCase):
    def test_spatialDenoising(self):
        clear = ClearNoise()
        images = clear.clear_noise()
        pix1 = images[0]
        pix2 = images[1]
        w, h = images[2]
        w -= 1
        h -= 1
        tot = 0
        for i in range(0, w):
            for j in range(0, h):
                tmp = abs(pix1[j, i] - pix2[j, i])
                tot += tmp / 255
        t = tot / (w * h)
        self.assertTrue(t <= 0.1)

#如果使用coverage测试则将这两行注释还原
# if __name__ == '__main__':
#     unittest.main()


