from functools import reduce
import numpy as np
import time
import numbers
import imageio
import random

def extract(cond, x):
    if isinstance(x, numbers.Number):
        return x
    else:
        return np.extract(cond, x)


