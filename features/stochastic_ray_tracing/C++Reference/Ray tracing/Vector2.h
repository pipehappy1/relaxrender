#pragma once
struct Vector2Int {
	int w;
	int h;

	Vector2Int(int w, int h) :w(w), h(h) {}
};

class Vector2 {
public:
	float x, y;
	Vector2(float x, float y);
	Vector2(float xy);
	Vector2();
	//Vector2& operator=(const Vector2& rhs);
	Vector2& operator+=(const Vector2& rhs);
	Vector2& operator-=(const Vector2& rhs);
	Vector2& operator*=(float rhs);
	Vector2& operator/=(float rhs);
	const Vector2 operator+(const Vector2& rhs)const;
	const Vector2 operator- (const Vector2& rhs)const;
	const Vector2 operator- ()const;
	const Vector2 operator* (float rhs)const;
	const Vector2 operator* (const Vector2& rhs)const;
	const Vector2 operator/ (float rhs)const;
	const Vector2 operator/ (const Vector2& rhs)const;

	const Vector2 operator/ (const Vector2Int& rhs)const;


	
	//ģ
	float magnitude() const;
	//ģ��ƽ��
	float sqrtMagnitude()const;
	//��һ��
	Vector2& Normalize();
	//��һ����ֻ��
	const Vector2 normalized() const;
	//���Բ�ֵ
	static const Vector2 Lerp(const Vector2& lhs, const Vector2& rhs, float k);

	//Ĭ��ֵ����
	static const Vector2 up;
	static const Vector2 down;
	static const Vector2 left;
	static const Vector2 right;
	static const Vector2 zero;
	static const Vector2 one;
};
