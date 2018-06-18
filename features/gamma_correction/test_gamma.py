#unittest为测试用的库
import unittest

import gamma_correction as gamma
from skimage import data,io
import matplotlib.pyplot as plt
import numpy as np
#gamma校正测试
class Test_gamma_correction(unittest.TestCase):

	#测试gamma_correction函数功能

	def test_gamma_correction(self):
		
		img0 = io.imread('1.png')
		#矫正后的标准图片
		img11 = io.imread('11.png')
		#gamma_correction矫正所得图片
		img1 = gamma.Gamma_correction().gamma_correction(img0,0.3)
		
		#比较两个图片是否相同
		self.assertEqual(img1.any(),img11.any())

if __name__=='__main__':
	unittest.main()
