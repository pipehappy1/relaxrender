import unittest

import gamma_correction as gamma
from skimage import data,io
import matplotlib.pyplot as plt
import numpy as np
#gamma校正测试
class Test_gamma_correction(unittest.TestCase):
	
    #对比测试
	def test_gamma_correction(self):
		img0 = io.imread('1.png')
		img11 = io.imread('11.png')
		img1 = gamma.Gamma_correction().gamma_correction(img0,0.3)
		
		self.assertEqual(img1.any(),img11.any())

if __name__=='__main__':
	unittest.main()
