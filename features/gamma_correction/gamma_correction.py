from skimage import data,io
import matplotlib.pyplot as plt
import numpy as np

 
class Gamma_correction():



	def gamma_correction(self,img,gamma):

		#-------gamma矫正算法
		#具体做法先归一化到1，然后gamma作为指数值求出新的像素值再还原

		gamma_table = [np.power(x/255.0,gamma)*255.0 for x in range(256)]
		gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
	
		#图片大小------(201,422,4)
		img_size = img.shape
		
		#复制img
		img1 = img.copy()
		
		for x in range(img_size[0]):
			for y in range(img_size[1]):
				#像素点的（0，1，2）通道中分别为该点的r,g,b像素值,4通道为景深此处用不到
				#通过gamma_table矫正其像素值实现gamma矫正
				#R（0通道）
				img1[x,y,0] = gamma_table[img[x,y,0]]
				#G（1通道）
				img1[x,y,1] = gamma_table[img[x,y,1]]
				#B（2通道）
				img1[x,y,2] = gamma_table[img[x,y,2]]

	
		#图形界面，可删
		#分割两个子图显示原图和gamma矫正后的图
		fig = plt.figure()
		ax1 = fig.add_subplot(211)
		ax1.imshow(img)
		#原图标题
		ax1.set_title("gamma = 1.0")
	
		#gamma矫正后的图片
		ax2 = fig.add_subplot(212)
		ax2.imshow(img1)
		#矫正后图片标题
		ax2.set_title("gamma = %f" %gamma)
		
		#调整三个子图的间距，默认适应
		plt.tight_layout()
		#设置显示
		plt.show()



		#返回gamma矫正后的图像

		return img1
