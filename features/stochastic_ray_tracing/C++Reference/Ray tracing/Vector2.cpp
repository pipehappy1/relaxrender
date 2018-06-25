#include <math.h>
#include "Vector2.h"
Vector2::Vector2(float x, float y) :x(x), y(y) {

}
Vector2::Vector2(float xy) : x(xy), y(xy)
{

}
Vector2::Vector2() : x(0), y(0) {

}
//Vector2& Vector2::operator=(const Vector2& rhs) {
//	this->x = rhs.x;
//	this->y = rhs.y;
//	return *this;
//}
Vector2& Vector2::operator+=(const Vector2& rhs) {
	*this = *this + rhs;
	return *this;
}
const Vector2 Vector2::operator+ (const Vector2& rhs)const {
	return Vector2(
		x + rhs.x,
		y + rhs.y);
}
Vector2& Vector2::operator-=(const Vector2& rhs) {
	*this = *this - rhs;
	return *this;
}
const Vector2 Vector2::operator- (const Vector2& rhs) const {
	return Vector2(
		x - rhs.x,
		y - rhs.y);
}
const Vector2 Vector2::operator-() const
{
	return Vector2(
		-x,
		-y);
}
const Vector2 Vector2::operator* (float rhs) const {
	return Vector2(
		x * rhs,
		y * rhs);
}
const Vector2 Vector2::operator*(const Vector2 & rhs) const
{
	return Vector2(
		x * rhs.x,
		y * rhs.y);
}
const Vector2 Vector2::operator/ (float rhs) const {
	return	Vector2(
		x / rhs,
		y / rhs);
}
const Vector2 Vector2::operator/(const Vector2 & rhs) const
{
	return	Vector2(
		x / rhs.x,
		y / rhs.y);
}
const Vector2 Vector2::operator/(const Vector2Int & rhs) const
{
	return	Vector2(
		x / rhs.w,
		y / rhs.h);
}
Vector2& Vector2::operator*=(float rhs) {
	*this = *this * rhs;
	return *this;
}
Vector2& Vector2::operator/=(float rhs) {
	*this = *this / rhs;
	return *this;
}
float Vector2::magnitude() const {
	return sqrt(x*x + y*y);
}
float Vector2::sqrtMagnitude()const {
	return x*x + y*y;
}
Vector2& Vector2::Normalize() {
	float m = magnitude();
	x /= m;
	y /= m;
	return *this;
}

const Vector2 Vector2::normalized() const {
	float m = magnitude();
	return Vector2(
		x / m,
		y / m
	);
}

const Vector2 Vector2::Lerp(const Vector2& lhs, const Vector2& rhs, float k) {
	float kp = 1 - k;
	return Vector2(
		kp*lhs.x + k*rhs.x,
		kp*lhs.y + k*rhs.y
	);
}

const Vector2 Vector2::up = Vector2(0, 1);
const Vector2 Vector2::down = Vector2(0, -1);
const Vector2 Vector2::left = Vector2(-1, 0);
const Vector2 Vector2::right = Vector2(1, 0);
const Vector2 Vector2::zero = Vector2(0, 0);
const Vector2 Vector2::one = Vector2(1, 1);