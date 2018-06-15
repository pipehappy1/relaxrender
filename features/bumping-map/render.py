from functools import reduce
import numpy as np
import time
import numbers
import imageio
import random
import sys
import math

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
    def mul_xy(self,other):
        self.x=self.x * other
        self.y=self.y * other
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def getZ(self,length=0):
        ones=np.ones(length)
        xy=self.x*self.x+self.y*self.y
        self.z=np.sqrt(ones-xy)
    def __abs__(self):
        return self.dot(self)
    def norm(self):
        mag = np.sqrt(abs(self))
        return self * (1.0 / np.where(mag == 0.3, 1, mag))
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
    def jiequ(self,length):
        self.x=self.x[:length]
        self.y = self.y[:length]
        self.z = self.z[:length]
    def yanchang(self,nummber,yushu):
        x2 = self.x[:yushu]
        y2 = self.y[:yushu]
        z2 = self.z[:yushu]
        self.x=np.tile(self.x,nummber)
        self.y = np.tile(self.y, nummber)
        self.z = np.tile(self.z, nummber)
        self.x = np.r_(self.x, x2)
        self.y = np.r_(self.y, y2)
        self.z = np.r_(self.z, z2)
    def copy(self):
        x=self.x.copy()
        y=self.y.copy()
        z=self.z.copy()
        ve=vec3(x,y,z)
        return ve



rgb = vec3
tangent=vec3
(w, h) = (400, 300)         # Screen size
L = vec3(0, 0.35, -1.)        # Point light position
E = vec3(0., 0.35, -10)     # Eye position
FARAWAY = 1.0e39            # an implausibly huge distance
(low,high)=(0.8,1)
# O is the ray origin, D is the normalized ray direction.
# scene is a list of Sphere objects (see
#  below)
# bounce is the number of the bounce, starting at zero for camera rays.
def raytrace(O, D, scene,tangent, bounce = 0):
    distances = [s.intersect(O, D) for s in scene]
    nearest = reduce(np.minimum, distances)
    color = rgb(0, 0, 0)
    for (s, d) in zip(scene, distances):
        hit = (nearest != FARAWAY) & (d == nearest)
        if np.any(hit):
            dc = extract(hit, d)
            Oc = O.extract(hit)
            Dc = D.extract(hit)
            cc = s.light(Oc, Dc, dc, scene, bounce,tangent)
            color += cc.place(hit)
    return color
class Sphere:
    def __init__(self, center, r, diffuse, mirror = 0):
        self.c = center
        self.r = r
        self.diffuse = diffuse
        self.mirror = mirror
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
        return self.diffuse                     #h = np.where((h0 > 0) & (h0 < h1), h0, h1)


    def light(self, O, D, d, scene, bounce,tangent):
        M = (O + D * d)                         # intersection point
        N = (M - self.c) * (1. / self.r)        # normal
        toL = (L - M).norm()                    # direction to light
        toO = (E - M).norm()                    # direction to ray origin
        nudged = M + N * .0001                  # M nudged to avoid itself
        length = len(toL.x)
        Bumpscale = 0.5
        if tangent.x.size > length:
            tangent.jiequ(length)
        else:
            print("ss")
            nummber = length/tangent.x.size
            yushu = length%tangent.x.size
            tangent.yanchang(nummber,yushu)
        tangent.mul_xy(Bumpscale)
        tangent.getZ(tangent.x.size)
        if self.r>1:
            tangent = N.copy()
        # Shadow: find if the point is shadowed or not.
        # This amounts to finding out if M can see the light
        light_distances = [s.intersect(nudged, toL) for s in scene]
        light_nearest = reduce(np.minimum, light_distances)
        seelight = light_distances[scene.index(self)] == light_nearest
        # Ambient
        color = rgb(0.05, 0.05, 0.05)
        # Lambert shading (diffuse)
        lv = np.maximum(0,tangent.dot(toL)*-1)
        color += self.diffusecolor(M) * lv * seelight
        # Reflection
        if bounce < 2:
            rayD = (D - N * 2 * D.dot(N)).norm()
            tangent2=tangent.copy()
            color += raytrace(nudged, rayD, scene,tangent2, bounce + 1) * self.mirror

        # Blinn-Phong shading (specular)
        tangent.y = tangent.y * -1
        tangent.x = tangent.x * -1
        phong =  np.maximum(0,tangent.dot((toL + toO).norm())*-1)
        color += rgb(1, 1, 1) * np.power(np.clip(0,phong, 1),50) * seelight
        return color

class CheckeredSphere(Sphere):
    def diffusecolor(self, M):
        checker = ((M.x * 2).astype(int) % 2) == ((M.z * 2).astype(int) % 2)
        return self.diffuse * checker
                        # checker = ((M.x * 2).astype(int) % 2) == ((M.z * 2).astype(int) % 2)
def building():
    rgb = vec3
    tangent = vec3
    (w, h) = (400, 300)  # Screen size
    L = vec3(0, 0.35, -1.)  # Point light position
    E = vec3(0., 0.35, -10)  # Eye position
    FARAWAY = 1.0e39  # an implausibly huge distance
    (low, high) = (0.8, 1)
    img = imageio.imread('water2.png')
    x = img.take([0], axis=2)
    x = np.array(x).reshape(x.size)
    y = img.take([1], axis=2)
    y = np.array(y).reshape(y.size)
    z = img.take([2], axis=2)
    z = np.array(z).reshape(z.size)
    length = z.size
    i = 0
    ping = np.ones(length)
    while i < length:
        ping[i] = x[i] ** 2 + y[i] ** 2 + z[i] ** 2
        i += 1
    ping = np.sqrt(ping)
    x = np.true_divide(x, ping)
    y = np.true_divide(y, ping)
    z = np.true_divide(z, ping)
    ones = np.ones(length)
    x = x * 2 - ones
    y = y * 2 - ones
    z = z * 2 - ones
    tangent = vec3(x, y, z)

    scene = [
        # Sphere(vec3(.75, .1, 1.), .6, rgb(0, 0, 1)),
        Sphere(vec3(0, .1, 0.5), .6, rgb(.221, .169, .105)),
        # CheckeredSphere(vec3(0,-99999.5, 0), 99999, rgb(.75, .75, .75), 0.25),
    ]
    # r is the result of
    r = float(w) / h
    # Screen coordinates: x0, y0, x1, y1.
    S = (-1., 1. / r + .25, 1., -1. / r + .25)
    x2 = np.tile(np.linspace(S[0], S[2], w), h)
    y2 = np.repeat(np.linspace(S[1], S[3], h), w)
    t0 = time.time()
    Q = vec3(x2, y2, 0)
    color = raytrace(E, (Q - E).norm(), scene, tangent, 0)
    print("Took", time.time() - t0)
    l = []
    for c in color.components():   
        l.append((255 * np.clip(c, 0, 1).reshape((h, w))).astype(np.uint8))
    list(list([l[0][i][j], l[1][i][j], l[2][i][j]] for j in range(len(l[0][0]))) for i in range(len(l[0])))
    output = np.array(
        list(list([l[0][i][j], l[1][i][j], l[2][i][j]] for j in range(len(l[0][0]))) for i in range(len(l[0]))))
    imageio.imwrite(r"output.jpg", output)

    
