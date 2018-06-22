from scipy import ndimage
from numpy import *
def blur(img,dimg,L=30):

      rows,cols,a=img.shape
      #r,g,b = img[100,100]
      #print(r,g,b)
      blured1 = img.copy()
      blured2 = img.copy()
      blured3 = img.copy()
      blured1[:,:,1] = ndimage.gaussian_filter(img[:,:,1],sigma = 4)
      blured2[:,:,1] = ndimage.gaussian_filter(img[:,:,1],6)
      blured3[:,:,1] = ndimage.gaussian_filter(img[:,:,1],8)
      for k in range(rows):
        for j in range(cols):             
          if dimg[k,j,0] > 3*L:
            img[k,j] = blured3[k,j]
          elif dimg[k,j,0] > 2*L:               
            img[k,j] = blured2[k,j]
          elif dimg[k,j,0] > L:      
