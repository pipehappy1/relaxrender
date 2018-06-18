from skimage import data,io
import matplotlib.pyplot as plt
import numpy as np

class Gamma_correction(): 

	def gamma_correction(self,img,gamma):
		#具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原-------gamma矫正算法
		gamma_table = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
		gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
	
		#图片大小------(201,422,4)
		img_size = img.shape
		#复制img
		img1 = img.copy()
		
		for x in range(img_size[0]):
			for y in range(img_size[1]):
				#像素点的（0，1，2）通道中分别为该点的r,g,b像素值，通过gamma_table矫正其像素值实现gamma矫正
				#R
				img1[x,y,0] = gamma_table[img[x,y,0]]
				#G
				img1[x,y,1] = gamma_table[img[x,y,1]]
				#B
				img1[x,y,2] = gamma_table[img[x,y,2]]
	
		fig = plt.figure()
		ax1 = fig.add_subplot(211)
		ax1.imshow(img)
		ax1.set_title("gamma = 1.0")
	
		ax2 = fig.add_subplot(212)
		ax2.imshow(img1)
		ax2.set_title("gamma = %f" %gamma)
		
		#调整三个子图的间距，默认适应
		plt.tight_layout()
		plt.show()
	
		return img1
