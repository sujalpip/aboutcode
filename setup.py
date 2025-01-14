#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='AboutCode',
    version='0.1.0',
    description='A family of FOSS projects to uncover data about software',
    author='Your Name',
    author_email='your.email@example.com',
    license='Apache-2.0',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
