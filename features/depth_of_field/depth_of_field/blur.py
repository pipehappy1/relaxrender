from scipy import ndimage
from numpy import *
def blur(img,dimg,L=30):

      rows,cols,a=img.shape
      #r,g,b = img[100,100]
      #print(r,g,b)
      blured1 = img.copy()
      blured2 = img.copy()
      blured3 = img.copy()
      
