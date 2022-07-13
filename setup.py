## This file is used to install the dependences from remote files

import setuptools


setuptools.setup(
    name="WAT",
    version="1.0",
    author="Gaurav Rai",
    author_email="",
    description="Writing Assistant Tool",
    long_description="Writing Assistant Tool for students, Helping them to practice their paragraph writing skills",
    url="https://github.com/lakeheadtoolsdev/WAT",
    packages=setuptools.find_packages(),
    install_requires=['transformers', 'sentencepiece', 'python-Levenshtein', 'sentence-transformers', 'fuzzywuzzy', 'pandas', 'numpy', 'scipy', 'protobuf==3.20.0', 'sklearn-pandas==1.5.0'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)