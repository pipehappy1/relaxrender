
import numpy as np

from .points import Vector, Point3D, Point, Points
from .color import Color
from .math import dist, sphere_sampling, ray_in_triangle

class RayCasting:
    def __init__(self, context):
        self.context = context

    def drive_raycasting(self, triangles):
        pass

    def cast_ray(self, input_x, input_y, triangles):
        pass

    def forward_history(self, history):
        pass


class SimpleReverseRayCasting(RayCasting):
    def __init__(self, context):
        super().__init__(context)

    def drive_raycasting(self, scene):
        input_xy = np.empty((self.context.raycasting_iteration, 2))
        output_color = np.empty((self.context.raycasting_iteration, 4))

        mesh = scene.mesh
        camera = scene.camera

        # translocate camera to origin.
        mesh.triangles = camera.relocate_world_by_camera(mesh.triangles)
        
        for index in range(self.context.raycasting_iteration):
            if index % 1000 == 0:
                print("working on ray: {}.".format(index))
            
            ray_samples, xy = camera.sample_vector()
            start_vector = ray_samples[0]
            input_xy[index, :] = xy[0]
            
            # every element of the history is a triple.
            # 1st element is the ray segment start point before the triangle.
            # 1st element is the ray segment end point on the triangle.
            # 2nd element is the index for the triangle in the mesh.
            ray_history = []

            power = 1

            res_vec, power = self.cast_ray(start_vector, ray_history, mesh, power)
            while res_vec is not None and res_vec.mode != 'place_holder' and power > 1e-3:
                res_vec, power = self.cast_ray(res_vec, ray_history, mesh, power)

            final_color = self.forward_history(ray_history, mesh)
            if final_color is not None:
                #color_data = np.concatenate((final_color.color,
                #                            Color.supported_color_space[final_color.mode]))
                output_color[index, :] = final_color.color

        return (input_xy, output_color)
            
            

    def cast_ray(self, start_vector, ray_history, mesh, power):
        p3d = start_vector.start
        nearest_dist = None
        nearest_ipoint = None
        nearest_triangle = None
        for tri in range(mesh.triangles.size()):
            result_ipoint = ray_in_triangle(start_vector, mesh.triangles[tri])
            if result_ipoint is not None:
                ppdist = dist(p3d, result_ipoint)
                if nearest_dist is None or ppdist < nearest_dist:
                    nearest_dist = ppdist
                    nearest_triangle = tri
                    nearest_ipoint = result_ipoint

        ret_power = mesh.textures[tri].damping_rate()*power

        if nearest_dist is None:
            return None, 0
        else:
            ray_history.append((p3d, nearest_ipoint, nearest_triangle))
            x, y, z = sphere_sampling(1)
            return Vector(nearest_ipoint,
                          Point3D(nearest_ipoint.data[0] + x,
                                  nearest_ipoint.data[1] + y,
                                  nearest_ipoint.data[2] + z,)), ret_power
            

    def forward_history(self, history, mesh):
        color = None
        while len(history) > 0:
            (p_start, p_end, tri) = history.pop()
            ttex = mesh.textures[tri]
            ttex_pos = mesh.texture_pos[tri]
            color = ttex.get_color(color, 0, 0, 0, 0, None, None)
        return color

            
        
