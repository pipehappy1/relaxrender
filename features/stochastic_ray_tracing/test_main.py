import somefunc.BMP as bmp
import somefunc.Model as md
import somefunc.basefunc as basef
from random import random
from time import time
import math as mt

#分辨率
iResolution=md.Vector2(800,640)
#采样点个数
SUB_SAMPLES=2
#最大深度
MAX_DEPTH=4
#最大样本循环
MAX_SAMPLE_LOOP=1
RESAMPLE_VALVE=1e-6
#gama值
GAMMA=2.2


def reflect(source,normal):
    temp1=normal.MultipleDecimal(2)
    temp2=md.vector3_instance.Dot(source,normal)
    temp2=temp1.MultipleDecimal(temp2)
    temp=source-temp2
    return temp

def cosWeightedSampleHemisphere(n):
    u1=random()
    u2=random()
    r=mt.sqrt(u1)
    theta=2*mt.pi*u2

    x=r*mt.cos(theta)
    y=r*mt.sin(theta)
    z=mt.sqrt(1-u1)
    
    a=md.Vector3()
    a.setSelf(n)
    b=md.Vector3()

    if (abs(a.x)<=abs(a.y)) and (abs(a.x)<=abs(a.z)):
        a.x=1
    elif abs(a.y)<=abs(a.z):
        a.y=1
    else:
        a.z=1
    
    a.Normalize()
    
    a.setSelf(md.vector3_instance.Cross(n,a))
    b.setSelf(md.vector3_instance.Cross(n,a))

    return (a.MultipleDecimal(x)+b.MultipleDecimal(y)+n.MultipleDecimal(z)).normalized()

"""
以下开始真正初始化和设置场景
"""
NUM_SPHERES=6	#球体数量
NUM_PLANES=6	#平面数量

spheres=[]
planes=[]



def initScene():
    
    for i in range(NUM_SPHERES):
        spheres.append(md.Sphere(i))

    for i in range(NUM_PLANES):
        planes.append(md.Plane())

    spheres[0].setSelf(md.Sphere(16.5,md.Vector3(27,16.5,47),md.Material(md.SPEC,md.ZERO_VECTOR3,md.ONE_VECTOR3,0.)))
    spheres[1].setSelf(md.Sphere(16.5,md.Vector3(73,16.5,78),md.Material(md.DIFF,md.ZERO_VECTOR3, md.Vector3(.75,1.,.75), 1.5)))
    spheres[2].setSelf(md.Sphere(5, md.Vector3(50,70,50), md.Material(md.SPEC, md.Vector3(5.7,5.7,5.7),md.ZERO_VECTOR3,0.)))
    spheres[3].setSelf(md.Sphere(14, md.Vector3(50, 14, 60), md.Material(md.SPEC,md.ZERO_VECTOR3, md.Vector3(0.5, 0.5, 0.), 2)))
    spheres[4].setSelf(md.Sphere(12, md.Vector3(92, 35, 65), md.Material(md.SPEC, md.ZERO_VECTOR3, md.Vector3(0.5, 0.5, 1.), 4)))
    spheres[5].setSelf(md.Sphere(18, md.Vector3(8, 25, 80), md.Material(md.SPEC, md.ZERO_VECTOR3, md.Vector3(1., 0.5, 0.5), 2)))

    planes[0].setSelf(md.Plane(md.Vector3(0, 0, 0),md.Vector3(0, 1, 0), md.Material(md.DIFF,md.ZERO_VECTOR3, md.ONE_VECTOR3, 0.)))
    planes[1].setSelf(md.Plane(md.Vector3(-7, 0, 0),md.Vector3(1, 0, 0), md.Material(md.DIFF,md.ZERO_VECTOR3,md.Vector3(.75, .25, .25), 0.)))
    planes[2].setSelf(md.Plane(md.Vector3(0,0,0), md.Vector3(0, 0, -1), md.Material(md.SPEC, md.ZERO_VECTOR3, md.Vector3(.75, .75, .75), 0.)))
    planes[3].setSelf(md.Plane(md.Vector3(107, 0, 0), md.Vector3(-1, 0, 0), md.Material(md.SPEC, md.ZERO_VECTOR3, md.Vector3(.75, .75, 1), 0.)))
    planes[4].setSelf(md.Plane(md.Vector3(0, 0, 185), md.Vector3(0, 0, 1), md.Material(md.DIFF, md.ZERO_VECTOR3, md.Vector3(1, 1, .75), 0.)))
    planes[5].setSelf(md.Plane(md.Vector3(0, 90, 0), md.Vector3(0, -1, 0), md.Material(md.DIFF, md.ZERO_VECTOR3, md.Vector3(.75,.75,.75), 0.)))

# def backgroud(dir):
#     return md.ZERO_VECTOR3

#光线与球相交，找到相交的球，返回相交球的ID(没找到返回-1)
def intersectByRay(ray):
    id=-1
    t=1e5#初始化为无限远
    for i in range(NUM_SPHERES):
        d=float(ray.IntersectWithSphere(spheres[i]))
        if d != 0. and d<t:
            id=i
            t=d
    
    for i in range(NUM_PLANES):
        d=float(ray.IntersectWithPlane(planes[i]))
        if d != 0. and d<t:
            t=d

    return id

def intersectWithAll(ray,t,normal,mat,nextPoint):
    id=-1
    isIdOfSphere=False
    t_=t
    t_.setSelf(1e5)#初始化为无限远

    for i in range(NUM_SPHERES):
        d=ray.IntersectWithSphere(spheres[i])
        if d!=0. and d<t_.x:
            id=i
            isIdOfSphere=True
            t_.setSelf(d)
    
    for i in range(NUM_PLANES):
        d=ray.IntersectWithPlane(planes[i])
        if d!=0. and d<t_.x:
            id =i
            isIdOfSphere=False
            t_.setSelf(d)

    if id>=0:
        nextPoint.setSelf(ray.origin+ray.dir.MultipleDecimal(t_.x))
        if isIdOfSphere:
            normal.setSelf((nextPoint-spheres[id].pos).normalized())
            mat.setSelf(spheres[id].mat)
        else:
            normal.setSelf(planes[id].normal)
            mat.setSelf(planes[id].mat)
    
    return id

camPos=md.Vector3(80.,40.8,172.)
cz=md.FORWARD_VECTOR3
cx=md.LEFT_VECTOR3
cy=md.UP_VECTOR3
aspectRatio=(float(iResolution.x))/(iResolution.y)
omegaRate=(1.0)/(mt.pi*0.5*(mt.pi*0.5-1))

#辐射度计算，即对应的灰度
def trace(u,v):
    
    rayDirTmp=(cx.MultipleDecimal(aspectRatio * (u * 2 - 1))+cy.MultipleDecimal((v * 2 - 1)*.5135)+cz).normalized()
    ray=md.Ray(camPos,rayDirTmp)

    #累积辐射度
    radiance=md.Vector3()
    #累计反射率
    reflectance=md.Vector3()
    reflectance.setSelf(md.ONE_VECTOR3)
    #相交处距离
    t=md.Float(0.)
    #相交面法线
    n=md.Vector3()
    #相交点
    nPoint=md.Vector3()
    #相交处材质
    mat=md.Material()

    #开始进行全场景的深度计算
    for depth in range(MAX_DEPTH):
        
        #如果没有和物体相交，返回背景的辐射度
        if intersectWithAll(ray,t,n,mat,nPoint)<0:
            radiance.setSelf(radiance+reflectance.MultipleVector3(md.ZERO_VECTOR3))
            break
        
        #累加这一次的辐射度
        radiance.setSelf(radiance+reflectance.MultipleVector3(mat.emission))

        color=md.Vector3()
        color.setSelf(mat.color)

        #根据光线与法线的方向判断是射入还是射出，并反转法线
        into = md.vector3_instance.Dot(n, ray.dir) < 0
        
        n1_=md.Vector3()
        n1_.setSelf(n)

        if into==False:
            n1_.setSelf(n1_.MultipleDecimal(-1))

        #将光线的原点移动到相交点
        ray.origin.setSelf(nPoint)

        #漫反射表面
        if mat.refl==md.DIFF:
            #反射率最大分量
            p=max(color.x,color.y,color.z)
            if(random()<p):
                reflectance.setSelf(reflectance.DivideDecimal(p))
            else:
                break

            ray.dir.setSelf(cosWeightedSampleHemisphere(n1_))
            reflectance.setSelf(reflectance.MultipleVector3(color))

            #强光照模型
            for i in range(NUM_SPHERES):
                s=spheres[i]
                if(s.mat.emission.sum()<=0):
                    #查找光源
                    continue
                centerL=s.pos-nPoint

                sw=md.Vector3()
                sw.setSelf(centerL.normalized())

                su=md.Vector3()
                su.setSelf(md.vector3_instance.Cross((md.UP_VECTOR3 if (abs(sw.x)>0.1) else md.RIGHT_VECTOR3),sw))

                sv=md.Vector3()
                sv.setSelf(md.vector3_instance.Cross(sw,su))

                cos_a_max=mt.sqrt(1-(s.radius**2)/centerL.sqrtMagnitude())
                cos_a=1-random()*(1-cos_a_max)
                sin_a=mt.sqrt(1-cos_a**2)
                phi=2*mt.pi*random()

                l=md.Vector3()
                l=su.MultipleDecimal(mt.cos(phi)*sin_a)+sv.MultipleDecimal(mt.sin(phi)*sin_a)+sw.MultipleDecimal(cos_a)
                l.Normalize()#自身归一化

                if intersectByRay(md.Ray(nPoint+l.MultipleDecimal(md.RAY_EPSILON),l))==i:
                    omega=mt.pi*(1-cos_a_max**2)*omegaRate
                    dot=md.vector3_instance.Dot(l,n1_)
                    radiance.setSelf(radiance+reflectance.MultipleVector3(s.mat.emission.MultipleDecimal(dot*omega)))

                    while intersectByRay(ray)==i:
                        ray.dir.setSelf(cosWeightedSampleHemisphere(n1_))
        #镜面反射表面
        elif mat.refl==md.SPEC:
            ray.dir.setSelf(reflect(ray.dir,n))
            reflectance.setSelf(reflectance.MultipleVector3(color))
        #折射表面
        else:
            ior=mat.ior
            ddn=md.vector3_instance.Dot(n1_,ray.dir)
            nnt=1/ior if into else ior
            
            rdir=md.Vector3()
            rdir.setSelf(reflect(ray.dir,n))

            cos2t=1.0-nnt**2*(1.0-ddn**2)
            
            #是否发生Total Internal Reflection
            if cos2t>0.0:
                #计算出折射光线的方向
                tdir=md.Vector3()
                tdir.setSelf((ray.dir.MultipleDecimal(nnt)-n1_.MultipleDecimal(ddn*nnt+mt.sqrt(cos2t))).normalized())

                R0=(ior-1)/(ior+1)
                R0*=R0
                #1 - cosθ
                c=1-(ddn*(-1) if into else md.vector3_instance.Dot(tdir,n))
                #菲涅尔项
                Re=R0+(1.0-R0)*(c**5)
                #反射概率
                P=0.25+0.5*Re

                #Russain roulette 俄罗斯优化
                if random()<P:
                    #选择反射
                    #反射系数
                    reflectance.setSelf(reflectance.MultipleDecimal(Re/P))
                    ray.dir.setSelf(rdir)
                else:
                    #选择折射
                    #折射系数
                    reflectance.setSelf(reflectance.MultipleVector3(color.MultipleDecimal((1.0-Re)/(1.0-P))))
                    ray.dir.setSelf(tdir)
            else:
                ray.dir.setSelf(rdir)
        #将光线向前推进一点，防止自相交
        ray.origin.setSelf(ray.origin+ray.dir.MultipleDecimal(md.RAY_EPSILON))   

    return radiance

def mainImage(fragCoord):
    color=md.Vector3()
    loop=0

    while color.sum()<=RESAMPLE_VALVE and loop<MAX_SAMPLE_LOOP:
        color.setSelf(md.ZERO_VECTOR3)
        #下面进行超采样
        for x in range(SUB_SAMPLES):
            for y in range(SUB_SAMPLES):
                #Tent Filter
                r1=2.*random()
                r2=2.*random()
                dx=( (1-mt.sqrt(2-r1)) if r1>1 else (mt.sqrt(r1)-1) )/SUB_SAMPLES
                dy=( (1-mt.sqrt(2-r2)) if r2>1 else (mt.sqrt(r2)-1) )/SUB_SAMPLES

                #生成相机光线  计算光线对应的辐射度
                color.setSelf(color+trace(fragCoord.x+dx/iResolution.x,fragCoord.y+dy/iResolution.y))

        color.setSelf(color.DivideDecimal(SUB_SAMPLES**2))
        loop=loop+1
    return color

def toBMPColor(dest,input):
    dest.r=(basef.clamp(input.x**(1 / GAMMA)) * 255 + 0.5)
    dest.g=(basef.clamp(input.y**(1 / GAMMA)) * 255 + 0.5)
    dest.b=(basef.clamp(input.z**(1 / GAMMA)) * 255 + 0.5)


    
def main():
    #初始化场景
    initScene()

    #初始化固定大小的列表
    sizeBmp = iResolution.x*iResolution.y
    bmpColors=[]
    for i in range(sizeBmp):
        bmpColors.append(bmp.BMPColor())

    timer=time()
    blackPoint=0
    grayPoint=0

    spp=SUB_SAMPLES**2
    y=0
    while y<iResolution.y :
        print("\r\rRendering"+"   "+str(spp)+"   "+str(100.*y / (iResolution.y - 1))+"%"+"              ",end="") 
        for x in range(iResolution.x):
            fragCoordd = md.Vector2( (float(x))/iResolution.x, (float(iResolution.y-1-y))/iResolution.y)
            c=mainImage(fragCoordd)
            if c.sum()<md.EPSILON:
                blackPoint=blackPoint+1
            if c.sum()<md.RAY_EPSILON:
                grayPoint=grayPoint+1
            toBMPColor(bmpColors[y*iResolution.x+x],c)
        y=y+1

    bmp.saveBitmap(iResolution.x,iResolution.y,bmpColors,"output-800_640.bmp")

    timer=time()-timer
    print("\nsuccess!\nuse time:\t"+str(timer)+" s")
    print("blackPoint num:\t"+str(blackPoint))

if __name__=="__main__":
    main()
