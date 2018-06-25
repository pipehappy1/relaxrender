export PYTHONPATH=./ # 将项目根目录作为PYTHONPATH
pytest --cov-report=html --cov=relaxrender --ignore=tests/test_relaxrender.py tests