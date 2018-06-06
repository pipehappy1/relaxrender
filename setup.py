from setuptools import find_packages
from setuptools import setup

install_requires = [
    'numpy',
    'imageio',
    'matplotlib',
    'scipy',
    'scikit-image'
]

tests_require = [
    'pytest',
]

setup(
    name="relaxrender",
    version="0.0.1",
    description="A ray-casting render lib",
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=install_requires,
)
