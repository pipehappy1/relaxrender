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

class vec3():
    def __init__(self, x, y, z):
        (self.x, self.y, self.z) = (x, y, z)
    def __mul__(self, other):
        return vec3(self.x * other, self.y * other, self.z * other)
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def __abs__(self):
        return self.dot(self)
    def norm(self):
        mag = np.sqrt(abs(self))
        return self * (1.0 / np.where(mag == 0, 1, mag))
    def components(self):
        return (self.x, self.y, self.z)
    def extract(self, cond):
        return vec3(extract(cond, self.x),
                    extract(cond, self.y),
                    extract(cond, self.z))
    def place(self, cond):
        r = vec3(np.zeros(cond.shape), np.zeros(cond.shape), np.zeros(cond.shape))
        np.place(r.x, cond, self.x)
        np.place(r.y, cond, self.y)
        np.place(r.z, cond, self.z)
        return r
rgb = vec3

(w, h) = (800, 600)         #图片大小
L = vec3(0, 0.9, 1)        #光源位置
E = vec3(0., 0.35, -1)     #视野位置
FARAWAY = 1.0e39            #无限长度

normalsource = imageio.imread(r"normal.png");
normalMap = np.array(normalsource)
normalX = normalsource.take([0], axis = 2)
normalX = np.array(normalX).reshape(normalX.size)
normalY = normalsource.take([1], axis = 2)
normalY = np.array(normalY).reshape(normalY.size)
normalZ = normalsource.take([2], axis = 2)
normalZ = np.array(normalZ).reshape(normalZ.size)
print (normalX)
print (normalY)
print (normalZ)
normalX = (normalX * 2 / 255) - 1
normalY = (normalY * 2 / 255) - 1
normalZ = (normalZ * 2 / 255) - 1
print (normalX.size)
print (normalY.size)
print (normalZ.size)

def raytrace(O, D, scene, bounce = 0):
    distances = [s.intersect(O, D) for s in scene]
    nearest = reduce(np.minimum, distances)
    color = rgb(0, 0, 0)
    for (sphere, d) in zip(scene, distances):
        hit = (nearest != FARAWAY) & (d == nearest)
        if np.any(hit):
            dc = extract(hit, d)
            Oc = O.extract(hit)
            Dc = D.extract(hit)
            cc = sphere.light(Oc, Dc, dc, scene, bounce)
            color += cc.place(hit)
    return color

class Sphere:
    def __init__(self, center, r, diffuse, mirror = 0.5):
        self.c = center
        self.r = r
        self.diffuse = diffuse
        self.mirror = mirror
        Sphere.countX = 0
        Sphere.countY = 0
        Sphere.countZ = 0


    def intersect(self, O, D):
        b = 2 * D.dot(O - self.c)
        c = abs(self.c) + abs(O) - 2 * self.c.dot(O) - (self.r * self.r)
        disc = (b ** 2) - (4 * c)
        sq = np.sqrt(np.maximum(0, disc))
        h0 = (-b - sq) / 2
        h1 = (-b + sq) / 2
        h = np.where((h0 > 0) & (h0 < h1), h0, h1)
        pred = (disc > 0) & (h > 0)
        return np.where(pred, h, FARAWAY)

    def diffusecolor(self, M):
        return self.diffuse

    def light(self, O, D, d, scene, bounce):
        M = (O + D * d)                         # 交点
        N = (M - self.c) * (1. / self.r)
        normal_x = normalX[0:97012]
        normal_y = normalY[0:97012]
        normal_z = normalZ[0:97012]

        N = vec3(normal_x, normal_y, normal_z)
        toL = (L - M).norm()                    # 光线方向
        toO = (E - M).norm()                    # 视野射线方向
        nudged = M + N * .0001                  # M nudged to avoid itself

        # 阴影并计算交点是否在阴影内
        light_distances = [s.intersect(nudged, toL) for s in scene]
        light_nearest = reduce(np.minimum, light_distances)
        seelight = light_distances[scene.index(self)] == light_nearest

        # 环境光
        color = rgb(0.05, 0.05, 0.05)

        #兰伯特光照
        lv = np.maximum(N.dot(toL) * -1, 0)
        color += self.diffusecolor(M) * lv * seelight

        # Blinn-Phong shading (specular)
        #phong = N.dot((toL + toO).norm()) * -1
        #color += rgb(1, 1, 1) * np.power(np.clip(0, phong, 1), 50) * seelight
        return color
def draw():
    scene = [ Sphere(vec3(0, .1, .5), .6, rgb(0.7, 0.7, 0.7))]
    #rgb(0.221, 0.169, 0.105)

    r = float(w) / h
    # Screen coordinates: x0, y0, x1, y1.
    S = (-1., 1. / r + .25, 1., -1. / r + .25)
    x = np.tile(np.linspace(S[0], S[2], w), h)
    y = np.repeat(np.linspace(S[1], S[3], h), w)

    t0 = time.time()
    Q = vec3(x, y, 0)
    color = raytrace(E, (Q - E).norm(), scene)
    print("Took", time.time() - t0)
    l=[]
    for c in color.components():
        l.append((255 * np.clip(c, 0, 1).reshape((h, w))) .astype(np.uint8))
    output=np.array(list(list([l[0][i][j],l[1][i][j],l[2][i][j]] for j in range(len(l[0][0]))) for i in range(len(l[0]))))
    imageio.imwrite(r"output.png",output)
    return 1

