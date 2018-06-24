组号：第四组 项目名字：stanford bunny 仓库链接：https://github.com/blueelphant/relaxrender/ 分支：agroup

运行前请安装pygame以及OpenGL库 并将项目安装到D盘根目录 windows下可用以下指令： pip install pygame pip install pyOpenGL

测试方法：运行test_main.py,test_objloader,test_light文件

测试覆盖率方法

打开 控制台 , cd 到项目根目录，之后设置 临时环境变量 PYTHONPATH 为当前目录，然后测试覆盖率

cd <项目根目录>

WINDOWS

set PYTHONPATH=<relaxrender绝对目录>

Linux

export PYTHONPATH=<relaxrender绝对目录>

cd features
cd bunny\

coverage run test_main.py coverage report -m 文件信息

读取OBJ文件代码：objloader.py 单元测试代码：test_main.py 待处理模型：bunny.obj 处理后产生动态渲染窗口 测试效果展示：

待处理图片：

bunny.obj

处理后图片：

bunny.png
