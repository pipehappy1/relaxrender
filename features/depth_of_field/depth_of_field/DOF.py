from depth_of_field import blur  as bl
from depth_of_field import getdepth as de
import matplotlib.pyplot as plt
import sys
import imageio as io
from sys import argv
from scipy import misc
def DepthOfField(im_path):
    point=[20,20]
    img = io.imread(im_path)
    dimg = de.depth(img,point)
    after = bl.blur(img,dimg)
    plt.imshow(after)
    plt.show()
