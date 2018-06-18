import unittest

import gamma_correction as gamma
from skimage import data,io
import matplotlib.pyplot as plt
import numpy as np

class Test_gamma_correction(unittest.TestCase):
	
	def test_gamma_correction(self):
		img0 = io.imread('1.png')
		img11 = io.imread('11.png')
		img1 = gamma.Gamma_correction().gamma_correction(img0,0.3)
		
		self.assertEqual(img1.any(),img11.any())
	
if __name__=='__main__':
	unittest.main()
