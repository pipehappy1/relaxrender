import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageStat as ImageStat
import os

"""
The bulk of this is taken from this Stack Overflow answer by fraxel:
http://stackoverflow.com/a/10575940/250962
"""


class Halftone:
    def __init__(self, path):
        """
        :param path: eg: ./src/1.jpeg
        """
        self.path = path
        
    def make(self, sample=10, scale=1, angles=[0, 15, 30, 45], antialias=False, style='color', percentage=0,filename_add='_halftoned'):
        """
            sample: 原始图像中的样本框大小（以像素为单位）。
            scale: 最大输出点直径是样本*比例
            angles: 每个屏幕通道应旋转4个角度的列表
            style: '颜色'或'灰度'
            antialias: true or false
            percentage: 从CMY频道中删除多少灰色分量并放入K频道
            filename_add: 输出文件名
        """

        # try:
        im = Image.open(self.path)
        # except IOError:
            # print("Cannot open such image...")
            # raise

        if style == 'grayscale':
            angles = angles[:1]
            gray_im = im.convert('L')  # mode:8位像素
            dots = self.halftone(gray_im, sample, scale, angles, antialias)
            new = dots[0]

        else:
            cmyk_im = im.convert('CMYK')
            cmyk_im_merge = self.gcr(cmyk_im, percentage)
            dots = self.halftone(cmyk_im_merge, sample, scale, angles, antialias)
            new = Image.merge('CMYK', dots)  # mode:4*8 位像素,颜色分离

        f, e = os.path.splitext(self.path)
        outfile = "%s%s%s" % (f, filename_add, e)
        new.save(outfile)
        
    def gcr(self, im, percentage):
        """
        gcr: 灰色组件更换
            返回从CMY通道中移除百分比灰色分量的CMYK图像
            并放入K频道，
            percentage = 80, (30, 100, 255, 0) >> (6, 76, 231, 24)
        """
        if not percentage:
            return im
        cmyk_arr = im.split()
        cmyk = []
        for i in range(4):
            cmyk.append(cmyk_arr[i].load())
        for x in range(im.size[0]):  # for x axis pixels
            for y in range(im.size[1]):  # for y axis pixels
                gray = min(cmyk[0][x, y], cmyk[1][x, y], cmyk[2][x, y]) * percentage / 100
                for i in range(3):
                    cmyk[i][x, y] -= int(gray)
                cmyk[3][x, y] = int(gray)
        return Image.merge('CMYK', cmyk_arr)
        
    def halftone(self, cmyk, sample, scale, angles, antialias):
        """
         返回cmyk图像的半色调图像列表。
         因此，样品= 1将保留原始图像分辨率，
        （但尺度必须大于1以允许点尺寸的变化）。
        """
        if antialias is True:
            antialias_scale = 4
            # 按照这个比例乘以图像的大小
            # 在合并时绘制和缩小
            scale *= antialias_scale

        dots = []

        for channel, angle in zip(cmyk.split(), angles):
            channel = channel.rotate(angle, expand=1)
            size = channel.size[0] * scale, channel.size[1] * scale
            half_tone = Image.new('L', size)
            draw = ImageDraw.Draw(half_tone)
            # 一次循环一个采样点，为每个采样点绘制一个圆圈：
            for x in range(0, channel.size[0], sample):
                for y in range(0, channel.size[1], sample):
                    # 我们抽样得到的等级：
                    box = channel.crop((x, y, x + sample, y + sample))

                    # 该框的平均等级（0-255）
                    mean = ImageStat.Stat(box).mean[0]

                    # 根据平均值绘制的圆的直径（0-1）：
                    diameter = (mean / 255) ** 0.5

                    # 我们将在此框中绘制圆框的大小：
                    box_size = sample * scale

                    # 我们将绘制的圆的直径：
                    #如果sample = 10且scale = 1，则这是（0-10）
                    draw_diameter = diameter * box_size

                    # 框左上角的位置，我们将在下面画圆：
                    # x_pos, y_pos = (x * scale), (y * scale)
                    box_x, box_y = (x * scale), (y * scale)

                    # 位于圈子的左上角和右下角：
                    #最大尺寸的圆将在其边缘有边缘绘图框的＃号
                    x1 = box_x + ((box_size - draw_diameter) / 2)
                    y1 = box_y + ((box_size - draw_diameter) / 2)
                    x2 = x1 + draw_diameter
                    y2 = y1 + draw_diameter

                    draw.ellipse([(x1, y1), (x2, y2)], fill=255)

            half_tone = half_tone.rotate(-angle, expand=1)
            width_half, height_half = half_tone.size

            # 要裁剪的图像的左上角和右下角：
            xx1 = (width_half - cmyk.size[0] * scale) / 2
            yy1 = (height_half - cmyk.size[1] * scale) / 2
            xx2 = xx1 + cmyk.size[0] * scale
            yy2 = yy1 + cmyk.size[1] * scale

            half_tone = half_tone.crop((xx1, yy1, xx2, yy2))

            if antialias is True:
                w = (xx2 - xx1) / antialias_scale
                h = (yy2 - yy1) / antialias_scale
                half_tone = half_tone.resize((int(w), int(h)), resample=Image.LANCZOS)
            dots.append(half_tone)
        return dots
