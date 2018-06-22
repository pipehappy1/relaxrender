from scipy import misc
import numpy as np
import math

def get_depth(rows,cols,row,col,point,maximum_dep):
    distance = math.sqrt((pow(row - point[0]*rows/100,2)+pow(col - point[1]*cols/100,2)))
    maximum_distance = math.sqrt(pow(rows,2)+pow(cols,2))
    return distance/maximum_distance*maximum_dep

def depth(img,point):