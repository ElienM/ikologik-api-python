from setuptools import find_packages, setup

setup(
	name='ikologik-api',
	version='0.0.2',
	packages=find_packages(include=['ikologik-api']),
	url='',
	license='MIT',
	author='Ikologik',
	author_email='development@ikologik.com',
	description='Ikologik api',
	setup_requires=['boto3==1.20.11', 'requests==2.26.0'],
	python_requires=">=3.9",
)
