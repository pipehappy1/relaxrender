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
set PYTHONPATH=<relaxrender绝对目录>
python <文件路径>
```

**Linux 运行文件方法之一：**

```
cd <项目根目录>
export PYTHONPATH=<relaxrender绝对目录>
python3 <文件路径>
```

### 代码量统计并排名

在 bash 下运行如下命令，即可生成 statistics.txt （按照代码量排名）

```shell
git log --format='%aN' | sort -r -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done | sort -n -r -k 4 -t: > statistics.txt
```

若想直接观看，可以直接运行如下命令：

```shell
git log --format='%aN' | sort -r -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done | sort -n -r -k 4 -t: 
```

示例如下：

```
pipehappy	added lines: 1844, removed lines: 0, total lines: 1844
tofar	added lines: 29, removed lines: 0, total lines: 29
pipehappy1	added lines: 21, removed lines: 0, total lines: 21
Liujiaohan	added lines: 8, removed lines: 0, total lines: 8
molscar	added lines: 4, removed lines: 0, total lines: 4
wenjiewang98228	added lines: 3, removed lines: 2, total lines: 1
```

