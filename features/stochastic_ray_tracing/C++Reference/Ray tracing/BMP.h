#pragma once
#pragma pack(2)//�����д������sizeof�ò�����ȷ�Ľ��  

struct BMPColor {
	BYTE b;
	BYTE g;
	BYTE r;
	BYTE a;

	BMPColor(BYTE r, BYTE g, BYTE b);
	BMPColor();

};
void saveBitmap(int w, int h, unsigned char *pData, const char * fileName);