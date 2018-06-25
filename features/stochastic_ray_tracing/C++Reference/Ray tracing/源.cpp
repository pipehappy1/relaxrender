#include <time.h>
#include <iostream>
#include <math.h>
#include <Windows.h>
#include <Random>
#include <process.h>
#include "Model.h"
#include "BMP.h"


//long threadNum = 0;

const Vector2Int iResolution = Vector2Int(640, 480);
#define SUB_SAMPLES 32
#define MAX_DEPTH 64
#define MAX_SAMPLE_LOOP 4
#define RESAMPLE_VALVE 1e-6
#define MAX_THREAD 4
#define GAMMA 2.2f


// Util functions
unsigned long seed = 0;
//取小数部分
inline float fract(float input) {
	float output = input - (int)input;
	return output > 0 ? output : (1 + output);
}
//裁剪到0-1
inline float clamp(float input) {
	return input < 0 ? 0 : (input < 1 ? input : 1);
}
//生成0-1的随机数
inline float myRand() {
	//return (rand() % int(1e4)) / 1e4;
	return fract(sin(seed++)*43758.5453123);
}

Vector3 reflect(const Vector3 &source, const Vector3 &normal) {
	return source - normal * 2 * Vector3::Dot(source, normal);
}

Vector3 cosWeightedSampleHemisphere(const Vector3 &n) {
	float u1 = myRand(), u2 = myRand();
	float r = sqrt(u1);
	float theta = 2 * PI * u2;

	float x = r * cos(theta);
	float y = r * sin(theta);
	float z = sqrt(1-u1);

	Vector3 a = n, b;

	if (abs(a.x) <= abs(a.y) && abs(a.x) <= abs(a.z))
		a.x = 1;
	else if (abs(a.y) <= abs(a.z))
		a.y = 1;
	else
		a.z = 1;
	a.Normalize();

	a = Vector3::Cross(n, a);
	b = Vector3::Cross(n, a);

	return (a * x + b * y + n * z).normalized();
}


// Scene Description
#define NUM_SPHERES 6	//球体数量
#define NUM_PLANES 6	//平面数量
Sphere *spheres[NUM_SPHERES];
Plane *planes[NUM_PLANES];

void initScene() {
	spheres[0] = new Sphere(16.5f, Vector3(27, 16.5f, 47), Material(SPEC, Vector3::zero, Vector3::one, 0.f));
	spheres[1] = new  Sphere(16.5f, Vector3(73, 16.5f, 78), Material(REFR, Vector3::zero, Vector3(.75f, 1.f, .75f), 1.5f));
	//spheres[2] = new  Sphere(600., Vector3(50, 689.3f, 50), Material(DIFF, Vector3::one*1.7f, Vector3::zero, 0.f));
	spheres[2] = new  Sphere(5, Vector3(50, 70, 50), Material(DIFF, Vector3::one*5.7f, Vector3::zero, 0.f));
	spheres[3] = new Sphere(14, Vector3(50, 14, 60), Material(REFR, Vector3::zero, Vector3(0.5f, 0.5f, 0), 2));
	spheres[4] = new Sphere(12, Vector3(92, 35, 65), Material(REFR, Vector3::zero, Vector3(0.5f, 0.5f, 1.f), 4));
	spheres[5] = new Sphere(18, Vector3(8, 25, 80), Material(SPEC, Vector3::zero, Vector3(1.f, 0.5f, 0.5f), 2));
	//spheres[6] = new Sphere(12, Vector3(50, 40, 80), Material(DIFF, Vector3::zero, Vector3(1.f, 0.5f, 0.5f), 2));

	planes[0] = new  Plane(Vector3(0, 0, 0), Vector3(0, 1, 0), Material(DIFF, Vector3(0.), Vector3::one, 0.));
	planes[1] = new  Plane(Vector3(-7, 0, 0), Vector3(1, 0, 0), Material(DIFF, Vector3(0.), Vector3(.75f, .25f, .25f), 0.));
	planes[2] = new  Plane(Vector3(0, 0, 0), Vector3(0, 0, -1), Material(SPEC, Vector3(0.), Vector3(.75f), 0.));
	planes[3] = new  Plane(Vector3(107, 0, 0), Vector3(-1, 0, 0), Material(SPEC, Vector3(0.), Vector3(.75f, .75f, 1), 0.));
	planes[4] = new  Plane(Vector3(0, 0, 185), Vector3(0, 0, 1), Material(SPEC, Vector3(0.), Vector3(1, 1, .75f), 0.));
	planes[5] = new  Plane(Vector3(0, 90, 0), Vector3(0, -1, 0), Material(DIFF, Vector3(0.), Vector3(.75f), 0.));
}
Vector3 background(const Vector3 &dir) {
	//return mix(vec3(0.), vec3(.9), .5 + .5 * dot(dir, vec3(0., 1., 0.)));
	//return texture(iChannel1, dir).rgb;
	return Vector3::zero;
}

// 光线与球相交，找到相交的球，返回相交球的ID(没找到返回false)
int intersect(const Ray &ray) {
	int id = -1;
	float t = 1e5;	//init as infinity
	for (int i = 0; i < NUM_SPHERES; i++) {
		float d = ray.Intersect(*spheres[i]);
		if (d != 0. && d < t) {
			id = i;
			t = d;
		}
	}

	for (int i = 0; i < NUM_PLANES; i++) {
		float d = ray.Intersect(*planes[i]);
		if (d != 0. && d < t) {
			t = d;
		}
	}
	return id;
}
// 光线与整个场景相交，找到相交的几何体，返回相交几何体的ID(没找到返回false)
int intersect(const Ray &ray, float &t, Vector3 &normal, Material &mat, Vector3 &nextPoint) {
	int id = -1;
	bool isIdOfSphere;
	t = 1e5;	//init as infinity
	for (int i = 0; i < NUM_SPHERES; i++) {
		float d = ray.Intersect(*spheres[i]);
		if (d != 0. && d < t) {
			id = i;
			isIdOfSphere = true;
			t = d;
		}
	}

	for (int i = 0; i < NUM_PLANES; i++) {
		float d = ray.Intersect(*planes[i]);
		if (d != 0. && d < t) {
			id = i;
			isIdOfSphere = false;
			t = d;
		}
	}

	if (id >= 0) {
		nextPoint = ray.origin + ray.dir * t;
		if (isIdOfSphere) {
			normal = (nextPoint - spheres[id]->pos).normalized();
			mat = spheres[id]->mat;
		}
		else {
			normal = planes[id]->normal;
			mat = planes[id]->mat;
		}
	}

	return id;
}


const Vector3 camPos = Vector3(50., 40.8, 172.);
const Vector3 cz = Vector3::forward;
const Vector3 cx = Vector3::left;
const Vector3 cy = Vector3::up;
const float aspectRatio = float(iResolution.w) / iResolution.h;

// 根据相机模型生成初始光线
//Ray generateRay(float x, float y) {
//	return Ray(camPos, ((cx * (aspectRatio * (x * 2 - 1)) + cy * (y * 2 - 1))*.5135f + cz).normalized());
//}
const float omegaRate = 1.0f / (PI*0.5f*(PI*0.5f - 1));

// 辐射度计算
Vector3& trace(float u, float v) {

	Ray ray(camPos, ((cx * (aspectRatio * (u * 2 - 1)) + cy * (v * 2 - 1))*.5135f + cz).normalized());

	Vector3 radiance;	// 累积辐射度
	Vector3 reflectance = Vector3::one;	// 累积反射率
	float t;	    // 相交处距离
	Vector3 n;			// 相交面的法线
	Vector3 nPoint;			// 相交点
	Material mat;   // 相交处材质

	for (int depth = 0; depth < MAX_DEPTH; depth++) {
		// 如果没有和物体相交，返回背景的辐射度
		if (intersect(ray, t, n, mat, nPoint) < 0) {
			radiance += reflectance * background(ray.dir);
			break;
		}

		// 累加这一次的辐射度
		radiance += reflectance * mat.emission;

		const Vector3 &color = mat.color;


		// 根据光线与法线的方向判断是射入还是射出，并反转法线
		bool into = Vector3::Dot(n, ray.dir) < 0;	// 光线是否从外部进来
		Vector3 nl = n;
		if (!into) {
			nl *= -1;
		}
		// 将光线的原点移动到相交点
		ray.origin = nPoint;


		if (mat.refl == DIFF) {				// 漫反射表面

			// 反射率最大分量
			float p = max(color.x, max(color.y, color.z));
			// Russain roulette
			if (myRand() < p) {
				reflectance /= p;
			}
			else
				break;

			ray.dir = cosWeightedSampleHemisphere(nl);
			reflectance *= color;

			// 强行光照模型
			for (int i = 0; i < NUM_SPHERES; i++) {
				const Sphere* s = spheres[i];
				if (s->mat.emission.sum() <= 0) continue; // 查找光源

				Vector3 centerL = s->pos - nPoint;

				Vector3 sw = centerL.normalized();
				Vector3 su = Vector3::Cross((fabs(sw.x) > .1 ? Vector3::up : Vector3::right), sw);
				Vector3 sv = Vector3::Cross(sw, su);

				float cos_a_max = sqrt(1 - (s->radius*s->radius / centerL.sqrtMagnitude()));
				float cos_a = 1 - myRand()*(1 - cos_a_max);
				float sin_a = sqrt(1 - cos_a*cos_a);
				float phi = 2 * PI * myRand();
				Vector3 l = su*cos(phi)*sin_a + sv*sin(phi)*sin_a + sw*cos_a;
				l.Normalize();
				if (intersect(Ray(nPoint, l)) == i) {  // shadow ray
					//float omega = 2 * PI* (1 - cos_a_max*cos_a_max);
					float omega = PI*(1 - cos_a_max*cos_a_max) *omegaRate;
					float dot = Vector3::Dot(l, nl);
					radiance += reflectance*s->mat.emission*(dot * omega);

					//reflectance *= 1 - dot;
					while (intersect(ray) == i) {
						ray.dir = cosWeightedSampleHemisphere(nl);
					}
				}
			}

		}
		else if (mat.refl == SPEC) {	    // 镜面反射表面

			ray.dir = reflect(ray.dir, n);
			reflectance *= color;
		}
		else {						    // 折射表面
			float ior = mat.ior;
			float ddn = Vector3::Dot(nl, ray.dir);
			float nnt = into ? 1 / ior : ior;
			Vector3 rdir = reflect(ray.dir, n);
			float cos2t = 1. - nnt * nnt * (1. - ddn * ddn);
			if (cos2t > 0.) {		// 是否发生Total Internal Reflection
									// 算出折射光线的方向
				Vector3 tdir = (ray.dir * nnt - nl * (ddn * nnt + sqrt(cos2t))).normalized();

				float R0 = (ior - 1) / (ior + 1);
				R0 *= R0;
				float c = 1 - (into ? -ddn : Vector3::Dot(tdir, n));	// 1 - cosθ
				float Re = R0 + (1. - R0) * c * c * c * c * c;	// 菲涅尔项

				float P = .25 + .5 * Re;			// 反射概率

				// Russain roulette
				if (myRand() < P) {				// 选择反射
					reflectance *= Re / P;		// 反射系数
					ray.dir = rdir;
				}
				else { 				        // 选择折射
					reflectance *= color * (1. - Re) / (1. - P);	// 折射系数
					ray.dir = tdir;
				}
			}
			else
				ray.dir = rdir;
		}

		// 将光线往前推进一点，防止自相交
		ray.origin += ray.dir * RAY_EPSILON;

	}

	return radiance;
}

Vector3 mainImage(const Vector2 &fragCoord) {
	Vector3 color = Vector3::zero;

	int loop = 0;
	do {
		color = Vector3::zero;
		// 超采样
		for (int x = 0; x < SUB_SAMPLES; x++) {
			for (int y = 0; y < SUB_SAMPLES; y++) {
				// Tent Filter
				float r1 = 2. * myRand();
				float r2 = 2. * myRand();
				float dx = ((r1 > 1 ? 1 - sqrt(2 - r1) : sqrt(r1) - 1) + x) / SUB_SAMPLES;
				float dy = ((r2 > 1 ? 1 - sqrt(2 - r2) : sqrt(r2) - 1) + y) / SUB_SAMPLES;
				//float dx = ((float)x) / SUB_SAMPLES;
				//float dy = ((float)y) / SUB_SAMPLES;

				//Vector2 jitter(dx / iResolution.w, dy / iResolution.h);

				//// 计算像素内采样点的uv坐标
				//Vector2 subuv = (fragCoord + jitter);

				// 生成相机光线
				// 计算光线对应的辐射度
				color += trace(fragCoord.x + dx / iResolution.w, fragCoord.y + dy / iResolution.h);
			}
		}

		color /= SUB_SAMPLES * SUB_SAMPLES;
		loop++;
	} while (color.sum()/*此处取模的平方*/ <= RESAMPLE_VALVE && loop < MAX_SAMPLE_LOOP);


	// Normalized pixel coordinates (from 0 to 1)
	//Vector2 uv = fragCoord / iResolution;

	// muiltpass 多次采样算出平均结果
	//color += texture(iChannel0, uv).rgb * float(iFrame);
	//return color / float(iFrame + 1);
	return color;
}

inline void toBMPColor(BMPColor &dest, const Vector3 &input) {
	dest.r = (BYTE)(clamp(pow(input.x, 1 / GAMMA)) * 255 + 0.5f);
	dest.g = (BYTE)(clamp(pow(input.y, 1 / GAMMA)) * 255 + 0.5f);
	dest.b = (BYTE)(clamp(pow(input.z, 1 / GAMMA)) * 255 + 0.5f);
}

//int xMax = 0;
//void pixelThread(void* data) {
//	//Vector2Int* dataP = (Vector2Int*)data;
//	//int x = dataP->w;
//	//int y = dataP->h;
//	int y = *(int*)(data);
//	for (int x = 0; x < iResolution.w; x++) {
//		if (xMax < x)xMax = x;
//		Vector3 c = mainImage(Vector2(((float)x) / iResolution.w, ((float)y) / iResolution.h));
//		if (c.sqrtMagnitude() < EPSILON)blackPoint++;
//		if (c.sqrtMagnitude() < RAY_EPSILON)grayPoint++;
//		bmpColor[y * iResolution.w + x] = toBMPColor(c);
//	}
//
//	threadNum--;
//	_endthread();
//}

int main() {
	// 初始化场景
	initScene();

	seed = clock() % 16;

	HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE);
	CONSOLE_CURSOR_INFO cursorInfo;
	GetConsoleCursorInfo(handle, &cursorInfo);
	cursorInfo.bVisible = false;
	SetConsoleCursorInfo(handle, &cursorInfo);


	long sizeBmp = iResolution.w*iResolution.h;
	BMPColor *bmpColor = new BMPColor[sizeBmp];

	long timer = clock();

	int blackPoint = 0;
	int grayPoint = 0;

	for (int y = 0; y < iResolution.h; y++) {
		fprintf(stderr, "\rRendering (%d spp) %5.4f%%\t", SUB_SAMPLES*SUB_SAMPLES, 100.*y / (iResolution.h - 1));
		for (int x = 0; x < iResolution.w; x++) {
			Vector3 c = mainImage(Vector2(((float)x) / iResolution.w, ((float)y) / iResolution.h));
			if (c.sum() < EPSILON)blackPoint++;
			if (c.sum() < RAY_EPSILON)grayPoint++;
			toBMPColor(bmpColor[y * iResolution.w + x], c);
		}
	}

	//while (threadNum > 0) {
	//	Sleep(1);
	//}

	saveBitmap(iResolution.w, iResolution.h, (unsigned char*)bmpColor, "output.bmp");

	//FILE *f;
	//fopen_s(&f, "image.txt", "w");// Write image to PPM file. 
	//fprintf(f, "P3\n%d %d\n%d\n", iResolution.w, iResolution.h, 255);
	//for (int i = 0; i < iResolution.w*iResolution.h; i++)
	//	fprintf(f, "%d %d %d ", toInt(color[i].x), toInt(color[i].y), toInt(color[i].z));

	//fclose(f);


	for (int i = 0; i < NUM_SPHERES; i++) {
		delete spheres[i];
	}
	for (int i = 0; i < NUM_PLANES; i++) {
		delete planes[i];
	}
	delete[] bmpColor;
	timer = clock() - timer;
	printf_s("\nsuccess!\nuse time:\t%lds%ldms", timer / 1000, timer % 1000);
	printf_s("\nblackPoint num:\t%d/%d", blackPoint, iResolution.w*iResolution.h);
	printf_s("\ngrayPoint num:\t%d/%d\n", grayPoint, iResolution.w*iResolution.h);
	system("output.bmp");
	system("pause");
	return 0;
}