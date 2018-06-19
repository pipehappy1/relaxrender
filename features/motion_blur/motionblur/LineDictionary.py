import numpy as np


class LineDictionary:
    def __init__(self):
        return

    def create_kernel(self, dim, angle):
        """
        创建卷积核矩阵
        """
        kernel = np.zeros((dim, dim), dtype=np.float32)
        if angle == 0:
            kernel[int(dim / 2), :] = 1
        elif angle == 45:
            for i in range(0, dim):
                kernel[i, dim - i - 1] = 1
        elif angle == 90:
            kernel[:, int(dim / 2)] = 1
        elif angle == 135:
            kernel = np.diag(np.ones(dim))
        return kernel
