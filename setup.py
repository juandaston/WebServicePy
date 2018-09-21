from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="WebServiceTest",
    version="1.0",
    install_requires=required
)