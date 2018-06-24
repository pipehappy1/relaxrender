
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
