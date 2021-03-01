import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "criptmodel", "VERSION.txt")) as fr:
    version = fr.read().strip()


setup(
    name="criptmodel",
    version=version,
    description="Python bindings for the CRIPT data models",
    url="https://github.com/C-Accel-CRIPT/cript-model-python",
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3.8"],
)
