#include <iostream>
#include <Windows.h>
#include "BMP.h"

void saveBitmap(int w, int h, unsigned char * pData, const char * fileName)
{

	// Define BMP Size  
	const int height = h;
	const int width = w;
	const int size = w*h * 4;
	double x, y;
	int index;

	// Part.1 Create Bitmap File Header  
	BITMAPFILEHEADER fileHeader;

	fileHeader.bfType = 0x4D42;
	fileHeader.bfReserved1 = 0;
	fileHeader.bfReserved2 = 0;
	fileHeader.bfSize = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + size;
	fileHeader.bfOffBits = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

	// Part.2 Create Bitmap Info Header  
	BITMAPINFOHEADER bitmapHeader = { 0 };

	bitmapHeader.biSize = sizeof(BITMAPINFOHEADER);
	bitmapHeader.biHeight = height;
	bitmapHeader.biWidth = width;
	bitmapHeader.biPlanes = 1;
	bitmapHeader.biBitCount = 32;
	bitmapHeader.biSizeImage = size;
	bitmapHeader.biCompression = 0; //BI_RGB  


									// Write to file  
	FILE *output;
	fopen_s(&output, fileName, "wb");

	if (output == NULL)
	{
		printf("Cannot open file!\n");
	}
	else
	{
		fwrite(&fileHeader, sizeof(BITMAPFILEHEADER), 1, output);
		fwrite(&bitmapHeader, sizeof(BITMAPINFOHEADER), 1, output);
		fwrite(pData, size, 1, output);
		fclose(output);
	}
}

BMPColor::BMPColor(BYTE r, BYTE g, BYTE b) :r(r), g(g), b(b), a(255) {}
BMPColor::BMPColor() : r(0), g(0), b(b), a(255) {}
