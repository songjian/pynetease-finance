import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynetease-finance",
    version="0.0.2",
    author="sj",
    author_email="songjian@codeorder.cn",
    description="获取网易财经网站数据。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/songjian/pynetease-finance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['certifi==2022.6.15',
    'idna==3.3',
    'numpy==1.23.1',
    'pandas==1.4.3',
    'python-dateutil==2.8.2',
    'charset-normalizer==2.1.0',
    'pytz==2022.1',
    'requests==2.28.1',
    'six==1.16.0',
    'urllib3==1.26.10',
    ],
    python_requires='>=3'
)
