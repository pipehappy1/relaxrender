# spatial denoising
## 空间去噪
#### 测试方法：运行test_spatialDenoising.py文件
#### 测试覆盖率方法
打开 控制台 , cd 到项目根目录，之后设置 临时环境变量 PYTHONPATH 为当前目录，然后测试覆盖率
```bash
cd <项目根目录>

# windows
set PYTHONPATH=<relaxrender绝对目录>
# linux
export PYTHONPATH=<relaxrender绝对目录>

cd features\
cd spatialDenoising\

coverage run test_spatialDenoising.py
coverage report -m
```

## 文件信息
- 去噪代码：clear_noise.py     
- 单元测试代码：test_spatialDenoising.py    
- 待处理图片：test.jpeg 
- 处理后的图片：result.jpeg    
- 预期图片：idel_result.bmp

## 测试效果展示：
### 待处理图片：
![test.jpg](https://github.com/nansanhao/relaxrender/blob/bgroup/features/spatialDenoising/test.jpeg)

### 处理后图片：
![test.jpg](https://github.com/nansanhao/relaxrender/blob/bgroup/features/spatialDenoising/result.jpeg)
