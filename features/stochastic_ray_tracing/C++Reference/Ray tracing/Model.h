#pragma once
#include "Vector3.h"
#include "Vector2.h"

// Constants
#define PI 3.14159265359
#define EPSILON 1e-6
#define RAY_EPSILON 1e-3

// Material Types (���������, ���淴�����, �������)
#define DIFF 0
#define SPEC 1
#define REFR 2

struct Material {
	int refl;	    // ��������(DIFF, SPEC, REFR)
	Vector3 emission;	// �Է���
	Vector3 color;		// ��ɫ
	float ior;		// ������

	Material(int refl, const Vector3 &emission, const Vector3 &color, float ior);
	Material();

	//Material& operator=(const Material& rhs);

};

struct Sphere {
	//public:
	float radius;	// �뾶
	Vector3 pos;	// λ��
	Material mat;	// ����

	Sphere(float radius, const Vector3 &pos, const Material &mat);
	Sphere();
};

struct Plane {
	Vector3 pos;		// λ��
	Vector3 normal;	// ����
	Material mat;	// ����

	Plane(const Vector3 &pos, const Vector3 &normal, const Material &mat);
	Plane();
};

class Ray {
public:
	Vector3 origin;	// ����ԭ��
	Vector3 dir; 	// ���߷���

	Ray(const Vector3 &origin, const Vector3 &dir);
	Ray();

	//Ray& operator=(const Ray& rhs);
	// �����������ཻ
	float Intersect(const Sphere &sphere) const;
	// ��������ƽ���ཻ
	inline float Intersect(const Plane &plane) const {
		float t = Vector3::Dot(plane.pos - origin, plane.normal) / Vector3::Dot(dir, plane.normal);
		return t > EPSILON ? t : 0;
	}
};