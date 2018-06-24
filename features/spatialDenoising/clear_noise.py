# coding:utf-8
import sys, os
from PIL import Image, ImageDraw
class ClearNoise:
    def __init__(self):
        pass

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
