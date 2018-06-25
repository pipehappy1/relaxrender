#pragma once
#pragma pack(2)//必须得写，否则sizeof得不到正确的结果  

struct BMPColor {
	BYTE b;
	BYTE g;
	BYTE r;
	BYTE a;

	BMPColor(BYTE r, BYTE g, BYTE b);
	BMPColor();

};
void saveBitmap(int w, int h, unsigned char *pData, const char * fileName);