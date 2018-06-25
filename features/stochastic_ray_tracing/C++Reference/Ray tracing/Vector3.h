#pragma once

class Vector3 {
public:
	float x, y, z;
	Vector3(float x, float y, float z);
	Vector3(float xyz);
	Vector3();
	//Vector3& operator=(const Vector3& rhs);
	Vector3& operator+=(const Vector3& rhs);
	Vector3& operator-=(const Vector3& rhs);
	Vector3& operator*=(float rhs);
	Vector3& operator*=(const Vector3& rhs);
	Vector3& operator/=(float rhs);
	const Vector3 operator+(const Vector3& rhs)const;
	const Vector3 operator- (const Vector3& rhs)const;
	const Vector3 operator- ()const;
	const Vector3 operator* (float rhs)const;
	const Vector3 operator* (const Vector3& rhs)const;
	const Vector3 operator/ (float rhs)const;
	const Vector3 operator/ (const Vector3& rhs)const;

	//和
	inline float sum() const {
		return x + y + z;
	}
	//模
	float magnitude() const;
	//模的平方
	float sqrtMagnitude()const;
	//归一化
	Vector3& Normalize();
	//归一化后，只读
	const Vector3& normalized() const;
	//点乘
	static float Dot(const Vector3& lhs, const Vector3& rhs);
	//叉乘
	static const Vector3 Cross(const Vector3& lhs, const Vector3& rhs);
	//线性插值
	static const Vector3 Lerp(const Vector3& lhs, const Vector3& rhs, float k);


	//默认值表列
	static const Vector3 up;
	static const Vector3 down;
	static const Vector3 left;
	static const Vector3 right;
	static const Vector3 forward;
	static const Vector3 back;
	static const Vector3 zero;
	static const Vector3 one;

};
