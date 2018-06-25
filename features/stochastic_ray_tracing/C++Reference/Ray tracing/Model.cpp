#include <math.h>
#include "Model.h"

Material::Material(int refl, const Vector3 & emission, const Vector3 & color, float ior) :refl(refl), emission(emission), color(color), ior(ior) {}

Material::Material() : refl(DIFF), emission(Vector3::zero), color(Vector3::zero), ior(0) {}
//Material& Material::operator=(const Material& rhs) {
//	refl = rhs.refl;
//	emission = rhs.emission;
//	color = rhs.color;
//	ior = rhs.ior;
//	return *this;
//}

Sphere::Sphere(float radius, const Vector3 & pos, const Material & mat) : radius(radius), pos(pos), mat(mat) {}

Sphere::Sphere() : radius(5), pos(Vector3::zero), mat(Material()) {}

Plane::Plane(const Vector3 & pos, const Vector3 & normal, const Material & mat) : pos(pos), normal(normal), mat(mat) {}

Plane::Plane() : pos(Vector3::zero), normal(Vector3::up), mat(Material()) {}

Ray::Ray(const Vector3 & origin, const Vector3 & dir) : origin(origin), dir(dir) {}

Ray::Ray() : origin(Vector3::zero), dir(Vector3::forward) {}

//Ray& operator=(const Ray& rhs);
// 检测光线与球相交

float Ray::Intersect(const Sphere & sphere) const {
	Vector3 op = sphere.pos - origin;
	float b = Vector3::Dot(op, dir);

	float delta = b * b - Vector3::Dot(op, op) + sphere.radius * sphere.radius;
	if (delta < 0)           // 光线与球体未相交
		return 0;
	else                      // 光线与球体相交
		delta = sqrt(delta);

	float distance;                  // 找到t最小的交点
	return (distance = b - delta) > EPSILON ? distance : ((distance = b + delta) > EPSILON ? distance : 0);
}
//Ray& Ray::operator=(const Ray& rhs) {
//	origin = rhs.origin;
//	dir = rhs.dir;
//
//	return *this;
//}

