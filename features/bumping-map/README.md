test.py是测试文件，render.py是凹凸映射函数，water2.png是法线纹理，output.jpg是输出。

another offline render.


conda env create --file environment.yml

conda install --file requirements.txt -y

pip install -e .

pytest --cov-report=html --cov=relaxrender --ignore=tests/test_relaxrender.py tests



注明：

若遇到找不到模块，或许可以采用如下运行方法，详细请看Python包管理相关知识

**Windows 运行方法之一：**

打开 cmd , cd 到项目根目录，之后设置 临时环境变量 PYTHONPATH 为当前目录，之后在根目录运行你的文件

示例：

```
# cmd
D:   # 磁盘号
cd <项目根目录>
set PYTHONPATH=./
python <文件路径>
```

**Linux 运行文件方法之一：**

```
cd <项目根目录>
export PYTHONPATH=./
python3 <文件路径>
```

