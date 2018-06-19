import math
import numpy as np
from scipy.signal import convolve2d
import imageio

from .LineDictionary import LineDictionary  # 导入{角度-核矩阵}的字典

lineLengths = [5, 10, 20]  # 线性长度

lineDict = LineDictionary()


def LinearMotionBlur_random(img):
    """
    随机选择模式进行模糊
    """
    lineLengthIdx = np.random.randint(0, len(lineLengths))
    lineLength = lineLengths[lineLengthIdx]
    lineAngle = randomAngle(lineLength)
    return LinearMotionBlur(img, lineLength, lineAngle)


def LinearMotionBlur(img, dim, angle, area=None, filename='picture_blur.jpg'):
    """
    依据参数进行运动模糊
    img为由PIL库导入的图片，dim为卷积核的宽度，angle为模糊方向，area为矩形模糊区域(包含四个元素的元组，默认为全图模糊)
    filename为导出的图片文件名(默认为'picture_blur.jpg'，导出到当前文件夹)
    """
    imgarray = np.array(img, dtype="float32")  # 将图片转换为数组
    imgshape = imgarray.shape
    kernel = LineKernel(dim, angle)  # 获得线性核
    if area is None:  # 若不传area参数，则默认对整张图片进行模糊
        r1, r2, c1, c2 = (0, imgshape[0], 0, imgshape[1])  # r1(row1)是矩形上边界，c1(colum1)是矩形左边界，r2是矩形下边界,c2是矩形右边界
    else:
        r1, r2, c1, c2 = area
    for d in range(3):
        # 对图像的RGB三个通道做循环处理
        # 只对area圈出的区域进行模糊，ing_conv_d的维度是(r2-r1)*(c2-c1)
        img_conv_d = convolve2d(imgarray[r1:r2, c1:c2, d], kernel, mode='same', boundary='symm')
        imgarray[r1:r2, c1:c2, d] = img_conv_d  # 将区域中的原像素值替换为卷积后的像素值
    imgarray = imgarray.astype("uint8")
    imageio.imwrite(filename, imgarray)  # 输出图片到指定文件
    img_blur = imageio.imread(filename)  # 返回模糊后的图片
    return img_blur


def LineKernel(dim, angle):
    """
    线性核
    """
    np.seterr(divide='ignore', invalid='ignore')  # 忽略数组中的零元素
    kernelwidth = dim  # 核的宽度
    kernelCenter = int(math.floor(kernelwidth / 2))  # 核的中心
    angle = sanitize_angleValue(kernelCenter, angle)  # 运动线的角度。将被定位到与给定内核大小相关的最近的一个。
    kernel = lineDict.create_kernel(kernelwidth, angle)
    normalizationFactor = np.count_nonzero(kernel)  # 返回kernel中非0元素的个数
    kernel = kernel / normalizationFactor  # 归一化
    return kernel


def sanitize_angleValue(kernelCenter, angle):
    """
    输入角度规范化
    """
    numDistinctLines = kernelCenter * 4
    angle = math.fmod(angle, 180.0)  # angle对180度取模
    validLineAngles = np.linspace(0, 180, numDistinctLines,
                                  endpoint=False)  # 把[0,180]区间等分为numDistinctLines份，如kerneldim=9时，分为16份
    angle = nearestValue(angle, validLineAngles)  # 找与输入角度最接近的角度
    return angle


def nearestValue(theta, validAngles):
    """
    获取与输入角度最接近的角度
    """
    idx = (np.abs(validAngles - theta)).argmin()
    return validAngles[idx]  # 返回角度值


def randomAngle(kerneldim):
    """
    随机获取角度
    """
    kernelCenter = int(math.floor(kerneldim / 2))
    numDistinctLines = kernelCenter * 4
    validLineAngles = np.linspace(0, 180, numDistinctLines,
                                  endpoint=False)  # 把[0,180]区间等分为numDistinctLines份，如kerneldim=9时，分为16份
    angleIdx = np.random.randint(0, len(validLineAngles))  # 角度的索引号(随机获得)
    return int(validLineAngles[angleIdx])  # 返回随机获取的角度
