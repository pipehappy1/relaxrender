运行前请安装以下两个库

pip install pygame

pip install PyOpenGL

因为代码采用了绝对寻址，如果有必要，请将relaxrender-bgroup文件夹安装至D盘根目录下

测试方法：运行test_main.py文件

测试覆盖率方法

打开 控制台 , cd 到项目根目录，之后设置 临时环境变量 PYTHONPATH 为当前目录，然后测试覆盖率

cd <项目根目录>

windows
set PYTHONPATH=<relaxrender绝对目录>

linux
export PYTHONPATH=<relaxrender绝对目录>

cd features
cd bunny\

coverage run test_main.py coverage report -m 文件信息

读取OBJ文件代码：objloader.py 单元测试代码：test_main.py 待处理模型：bunny.obj 处理后产生动态渲染窗口 测试效果展示：

待处理图片：

bunny.obj

处理后图片：

bunny.png
