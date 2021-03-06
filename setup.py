#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


__version__ = "1.0.0"


def get_description():
    with open("README.md", "r") as f:
        desc = f.read()
    return desc


setup(
    name="markdown-wavedrom",
    version=__version__,
    license="MIT License",
    description="Support for WaveDrom in Python Markdown",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    author="Maximilian Köstler",
    author_email="maximilian@koestler.dev",
    python_requires=">=3.6",
    url="https://github.com/MaximilianKoestler/markdown-wavedrom",
    packages=find_packages(exclude=["test*"]),
    include_package_data=False,
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Utilities",
    ],
    keywords=["Markdown", "WaveDrom", "MkDocs"],
    install_requires=["Markdown"],
    extras_require={},
)
