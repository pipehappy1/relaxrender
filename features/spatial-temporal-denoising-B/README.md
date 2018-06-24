局部降噪B组

conda env create --file environment.yml

conda install --file requirements.txt -y

pip install -e .

测试方法：
pytest --cov-report=html --cov=temporal_denoising --ignore=temporal_denoising.py test_denoising.py
根据输出的html可知覆盖率达到100%
不过依旧是个很简单的实现
还有待进一步优化
有一些备用图像可以测试看看