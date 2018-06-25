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

	//��
	inline float sum() const {
		return x + y + z;
	}
	//ģ
	float magnitude() const;
	//ģ��ƽ��
	float sqrtMagnitude()const;
	//��һ��
	Vector3& Normalize();
	//��һ����ֻ��
	const Vector3& normalized() const;
	//���
	static float Dot(const Vector3& lhs, const Vector3& rhs);
	//���
	static const Vector3 Cross(const Vector3& lhs, const Vector3& rhs);
	//���Բ�ֵ
	static const Vector3 Lerp(const Vector3& lhs, const Vector3& rhs, float k);


	//Ĭ��ֵ����
	static const Vector3 up;
	static const Vector3 down;
	static const Vector3 left;
	static const Vector3 right;
	static const Vector3 forward;
	static const Vector3 back;
	static const Vector3 zero;
	static const Vector3 one;

};
