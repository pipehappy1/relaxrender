import test3 as gamma
from skimage import data,io
import matplotlib.pyplot as plt
import numpy as np

#读取图片
img0 = io.imread('1.png')

img = gamma.gamma_correction(img0,0.3)