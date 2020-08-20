from setuptools import setup, find_packages

setup(
    name='scrapy_utils',
    version="1.0",
    description='Scrapy Utils Framework',
    packages=find_packages(exclude=[]),
    author='Zhui',
    author_email='asd4988@qq.com',
    license='MIT',
    package_data={'': ['*.*']},
    url='#',
    zip_safe=False,
    install_requires=[
        'redis==2.10.6',
        'six>=1.5.2',
        'redis-py-cluster==1.3.6',
        'pymongo',
        'pymysql',
        'mysqlclient'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
