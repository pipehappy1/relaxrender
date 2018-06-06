import numpy as np
import imageio

class NormalizedWriter:
    def __init__(self, context):
        self.ctx = context

    def write(self, input_xy, output_color, file_name=None):
        """
        input_xy is a Nx2 array. Elements in input_xy has a value in [-1, 1]
        output_color is a at least Nx4 array.
        """
        (xy_size, xy_width) = input_xy.shape
        (color_size, color_width) = output_color.shape
        if xy_size != color_size:
            raise ValueError


        sample_size = input_xy.shape[0]

        if file_name is None:
            file_name = 'output' + '.' + self.ctx.writer_output_device

        img = None
        if self.ctx.writer_color_mode == 'RGB':
            img = np.zeros((self.ctx.output_height,
                            self.ctx.output_width,
                            3))

        posx = np.floor(input_xy[:, 0] *(self.ctx.output_width/2) + self.ctx.output_width/2)
        posy = np.floor(self.ctx.output_height/2 - input_xy[:, 1] *(self.ctx.output_height/2))

        index1d = posx + posy*self.ctx.output_width

        sort_order = np.argsort(index1d)
        sort_index1d = index1d[sort_order]
        sort_color = output_color[sort_order, :]

        step_index = 0
        for i in range(self.ctx.output_height):
            for j in range(self.ctx.output_width):
                cpos = j + i * self.ctx.output_width

                if step_index == sample_size:
                    break

                if sort_index1d[step_index] != cpos:
                    continue
        
                end_step_index = step_index
                while end_step_index < sample_size and sort_index1d[end_step_index] == cpos:
                    end_step_index += 1
                
                res_color = np.mean(sort_color[step_index:end_step_index, :], axis=0)
                
                img[i, j, 0] = res_color[0]
                img[i, j, 1] = res_color[1]
                img[i, j, 2] = res_color[2]

                step_index = end_step_index

        writer = imageio.get_writer('./'+file_name)
        writer.append_data((img*255).astype(np.uint8))
        writer.close()
