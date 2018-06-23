#import Model as md
import sys
from math import sqrt

__author__="lizelin"

class Vector3:
    x=0.0
    y=0.0
    z=0.0
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x=x
        self.y=y
        self.z=z

    def setSelf(self,targetVector3):
        self.x=targetVector3.x
        self.y=targetVector3.y
        self.z=targetVector3.z
        
    """
    以下为操作符重载
    """
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"

    #左加
    def __add__(self, data):
        temp=Vector3(self.x+data.x,self.y+data.y,self.z+data.z)
        return temp
    #右加
    # def __radd__

    def __sub__(self, data):  
        temp=Vector3(self.x-data.x,self.y-data.y,self.z-data.z)
        return temp

    def __mul__(self, data):
        if type(data)==vector3_instance:
            return Vector3(self.x*data.x,self.y*data.y,self.z*data.z)
        elif type(data)==float or type(data)==int:
            return Vector3(self.x*data,self.y*data,self.z*data)


    def __iadd__(self, data):
        if type(data)==vector3_instance:
            print(type(data))
            return Vector3(self.x+data.x,self.y+data.y,self.z+self.z)
        elif type(data)==float or type(data)==int:
            return self+data
        else:
            return self




    """
    以上为操作符重载
    """

    def dot(self,target):
        self.x=self.x*target.x
        self.y=self.y*target.y
        self.z=self.z*target.z
        return self
    
    def sum(self):
        return self.x+self.y+self.z


    def magnitude(self):
        return sqrt(self.x*self.x+self.y*self.y+self.z*self.z)

    def sqrtMagnitude(self):
        return self.x*self.x+self.y*self.y+self.z*self.z

    def normalized(self):
        m=self.magnitude()
        temp=Vector3(self.x/m,self.y/m,self.z/m)
        return temp

    #计算该向量和某一向量加法的结果，原向量不改变
    def AddVector3(self,target):
        temp=Vector3(self.x+target.x,self.y+target.y,self.z+target.z)
        return temp
    #计算该向量和某一向量减法的结果，原向量不改变
    def MinusVector3(self,target):
        temp=Vector3(self.x-target.x,self.y-target.y,self.z-target.z)
        return temp
    def MultipleVector3(self,data):
        temp=Vector3(self.x*data.x,self.y*data.y,self.z*data.z)
        return temp
    def DivideVector3(self,data):
        temp=Vector3(self.x/data.x,self.y/data.y,self.z/data.z)
        return temp
    #计算该向量和一个常数的乘积，原向量不改变
    def MultipleDecimal(self,data):
        temp=Vector3(self.x*data,self.y*data,self.z*data)
        return temp
    #计算该向量和一个常数的除数结果，原向量不改变
    def DivideDecimal(self,data):
        temp=Vector3(self.x/data,self.y/data,self.z/data)
        return temp
    def Normalize(self):
        m=self.magnitude()
        self.x=self.x/m
        self.y=self.y/m
        self.z=self.z/m
        return self
        

    def Dot(self,lhs,rhs):
        temp=lhs.x*rhs.x+lhs.y*rhs.y+lhs.z*rhs.z
        return temp

    def Cross(self,lhs,rhs):
        temp=Vector3(lhs.y*rhs.z - lhs.z*rhs.y,lhs.z*rhs.x - lhs.x*rhs.z,lhs.x*rhs.y - lhs.y*rhs.x)
        return temp
        


      

class Vector2:
    x=0.0
    y=0.0
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def setSelf(self,targetVector2):
        self.x=targetVector2.x
        self.y=targetVector2.y

    def magnitude(self):
        return sqrt(self.x*self.x+self.y*self.y)
    def sqrtMagnitude(self):
        return self.x*self.x+self.y*self.y
    #返回归一化的结果，但是自身不归一化
    def normalized(self):
        m=self.magnitude()
        temp=Vector2(self.x/m,self.y/m)
        return temp
    
    #自身归一化
    def Normalize(self):
        m=self.magnitude()
        self.x=self.x/m
        self.y=self.y/m
        self.z=self.z/m
        return self
    

#零三维向量
ZERO_VECTOR3=Vector3(0.0,0.0,0.0)
#一三维向量
ONE_VECTOR3=Vector3(1.0,1.0,1.0)
#六个常用方向的三维向量
UP_VECTOR3=Vector3(0.0,1.0,0.0)
DOWN_VECTOR3=Vector3(0.0,-1,0.0)
LEFT_VECTOR3=Vector3(-1.0,0.0,0.0)
RIGHT_VECTOR3=Vector3(1.0,0.0,0.0)
FORWARD_VECTOR3=Vector3(0.0,0.0,-1.0)
BACK_VECTOR3=Vector3(0.0,0.0,1.0)
vector3_instance=Vector3()
vector2_instance=Vector2()

if __name__=="__main__":
    tmp=Vector3(1,1,1)
    a=2
    print(tmp)
    print(type(tmp))
    print(type(a))
    tmp+=a
    print(tmp)
    print(type(tmp.x)==int)
    