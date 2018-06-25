#pragma once
#include "Vector3.h"
#include "Vector2.h"

// Constants
#define PI 3.14159265359
#define EPSILON 1e-6
#define RAY_EPSILON 1e-3

// Material Types (漫反射表面, 镜面反射表面, 折射表面)
#define DIFF 0
#define SPEC 1
#define REFR 2

struct Material {
	int refl;	    // 表面属性(DIFF, SPEC, REFR)
	Vector3 emission;	// 自发光
	Vector3 color;		// 颜色
	float ior;		// 折射率

	Material(int refl, const Vector3 &emission, const Vector3 &color, float ior);
	Material();

	//Material& operator=(const Material& rhs);

};

struct Sphere {
	//public:
	float radius;	// 半径
	Vector3 pos;	// 位置
	Material mat;	// 材质

	Sphere(float radius, const Vector3 &pos, const Material &mat);
	Sphere();
};

struct Plane {
	Vector3 pos;		// 位置
	Vector3 normal;	// 法线
	Material mat;	// 材质

	Plane(const Vector3 &pos, const Vector3 &normal, const Material &mat);
	Plane();
};

class Ray {
public:
	Vector3 origin;	// 光线原点
	Vector3 dir; 	// 光线方向

	Ray(const Vector3 &origin, const Vector3 &dir);
	Ray();

	//Ray& operator=(const Ray& rhs);
	// 检测光线与球相交
	float Intersect(const Sphere &sphere) const;
	// 检测光线与平板相交
	inline float Intersect(const Plane &plane) const {
		float t = Vector3::Dot(plane.pos - origin, plane.normal) / Vector3::Dot(dir, plane.normal);
		return t > EPSILON ? t : 0;
	}
};