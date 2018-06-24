# coding:utf-8
import sys, os
from PIL import Image, ImageDraw
class ClearNoise:
    def __init__(self):
        pass
    
    # 判断噪点
    # 将灰度值与周围灰度值相似度较小的点认为是噪点
    def clearNoise_2(self, img, radius, m):

        pix = img.load()
        w, h = img.size
        w -= 1
        h -= 1

        # 认为这个点是噪点
        for i in range(0, w):
            for j in range(0, h):
                sim = -1
                for k in range(i - radius, i + radius):
                    if k < 1 or k > w:
                        continue
                    for q in range(j - radius, j + radius):
                        if q <= 1 or q > h:
                            continue
                        if abs(pix[k, q] - pix[i, j]) < 40:
                            sim += 1
                # 该点与周围点相似度较小，认为是噪点
                if sim < m:
                    tmp = self.mid_of_rec(pix, i, j, radius, w, h)
                    pix[i, j] = tmp

    def mid_of_rec(self, pix, x, y, radius, w, h):
        p = []
        for i in range(x - radius, x + radius):
            if i < 1 or i > w:
                continue
            for j in range(y - radius, y + radius):
                if j <= 1 or j > h:
                    continue
                # 排除极值点
                if pix[i, j] > 15 and pix[i, j] < 230:
                    p.append(pix[i, j])

        p.sort()
        m = len(p) // 2
        return (p[m] + p[-m]) // 2	

    def clear_noise(self):

        # 打开图片
        image = Image.open("./test.jpeg").convert('L')
        img = Image.open("./ideal_result.bmp").convert('L')

        # 采用中值去噪
        self.clearNoise_2(image, 3, 9)

        # 保存图片
        image.save("./result.jpeg")
        pix_1=image.load()
        pix_2=img.load()

        image.close()
        img.close()

        return (pix_1, pix_2,image.size)


