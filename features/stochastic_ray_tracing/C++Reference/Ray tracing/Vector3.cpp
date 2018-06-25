#include <math.h>
#include "Vector3.h"
Vector3::Vector3(float x, float y, float z) :x(x), y(y), z(z) {

}
Vector3::Vector3(float xyz) : x(xyz), y(xyz), z(xyz)
{

}
Vector3::Vector3() : x(0), y(0), z(0) {

}
//Vector3& Vector3::operator=(const Vector3& rhs) {
//	this->x = rhs.x;
//	this->y = rhs.y;
//	this->z = rhs.z;
//	return *this;
//}
Vector3& Vector3::operator+=(const Vector3& rhs) {
	*this = *this + rhs;
	return *this;
}
const Vector3 Vector3::operator+ (const Vector3& rhs)const {
	return Vector3(
		x + rhs.x,
		y + rhs.y,
		z + rhs.z);
}
Vector3& Vector3::operator-=(const Vector3& rhs) {
	*this = *this - rhs;
	return *this;
}
const Vector3 Vector3::operator- (const Vector3& rhs) const {
	return Vector3(
		x - rhs.x,
		y - rhs.y,
		z - rhs.z);
}
const Vector3 Vector3::operator-() const
{
	return Vector3(
		-x,
		-y,
		-z);
}
const Vector3 Vector3::operator* (float rhs) const {
	return Vector3(
		x * rhs,
		y * rhs,
		z * rhs);
}
const Vector3 Vector3::operator*(const Vector3 & rhs) const
{
	return Vector3(
		x * rhs.x,
		y * rhs.y,
		z * rhs.z);
}
const Vector3 Vector3::operator/ (float rhs) const {
	return	Vector3(
		x / rhs,
		y / rhs,
		z / rhs);
}
const Vector3 Vector3::operator/(const Vector3 & rhs) const
{
	return	Vector3(
		x / rhs.x,
		y / rhs.y,
		z / rhs.z);
}
Vector3& Vector3::operator*=(float rhs) {
	*this = *this * rhs;
	return *this;
}
Vector3 & Vector3::operator*=(const Vector3 & rhs)
{
	*this = *this * rhs;
	return *this;
}
Vector3& Vector3::operator/=(float rhs) {
	*this = *this / rhs;
	return *this;
}

//ºÍ

float Vector3::magnitude() const {
	return sqrt(x*x + y*y + z*z);
}
float Vector3::sqrtMagnitude()const {
	return x*x + y*y + z*z;
}
Vector3& Vector3::Normalize() {
	float m = magnitude();
	x /= m;
	y /= m;
	z /= m;
	return *this;
}

const Vector3& Vector3::normalized() const {
	float m = magnitude();
	return Vector3(
		x / m,
		y / m,
		z / m
	);
}

float Vector3::Dot(const Vector3& lhs, const Vector3& rhs) {
	return lhs.x*rhs.x + lhs.y*rhs.y + lhs.z*rhs.z;
}

const Vector3 Vector3::Cross(const Vector3& lhs, const Vector3& rhs) {
	return Vector3(
		lhs.y*rhs.z - lhs.z*rhs.y,
		lhs.z*rhs.x - lhs.x*rhs.z,
		lhs.x*rhs.y - lhs.y*rhs.x
	);
}
const Vector3 Vector3::Lerp(const Vector3& lhs, const Vector3& rhs, float k) {
	float kp = 1 - k;
	return Vector3(
		kp*lhs.x + k*rhs.x,
		kp*lhs.y + k*rhs.y,
		kp*lhs.z + k*rhs.z
	);
}

const Vector3 Vector3::up = Vector3(0, 1, 0);
const Vector3 Vector3::down = Vector3(0, -1, 0);
const Vector3 Vector3::left = Vector3(-1, 0, 0);
const Vector3 Vector3::right = Vector3(1, 0, 0);
const Vector3 Vector3::forward = Vector3(0, 0, -1);
const Vector3 Vector3::back = Vector3(0, 0, 1);
const Vector3 Vector3::zero = Vector3(0, 0, 0);
const Vector3 Vector3::one = Vector3(1, 1, 1);