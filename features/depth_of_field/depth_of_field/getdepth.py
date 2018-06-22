from scipy import misc
import numpy as np
import math

def get_depth(rows,cols,row,col,point,maximum_dep):
    distance = math.sqrt((pow(row - point[0]*rows/100,2)+pow(col - point[1]*cols/100,2)))
    maximum_distance = math.sqrt(pow(rows,2)+pow(cols,2))
    return distance/maximum_distance*maximum_dep

def depth(img,point):
    dimg = img.copy()
    dimg = dimg[:, :, :, np.newaxis]
    rows, cols, a = img.shape
    #print("%d" % cols)
    for row_tag in range(rows):
      for col_tag in range(cols):
        dimg[row_tag,col_tag,0] = get_depth(rows,cols,row_tag,col_tag,point,200)
    print("Calculate depth data successful.")
    return dimg