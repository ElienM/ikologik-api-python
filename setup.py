from setuptools import find_packages, setup

setup(
    name='ikologikapi',
    version='1.1.30',
    packages=find_packages(include=['ikologikapi*']),
    url='',
    license='MIT',
    author='Ikologik',
    author_email='development@ikologik.com',
    description='Ikologik API',
    install_requires=['boto3==1.20.11', 'requests==2.26.0'],
    python_requires=">=3.9",
)
