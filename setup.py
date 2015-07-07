#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='cooperhewitt.api',
    namespace_packages=['cooperhewitt'],
    version='0.4.3',
    description='Simple Python wrapper for Cooper-Hewitt API',
    author='Smithsonian Cooper-Hewitt National Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-api',
    install_requires=[
        'requests'
        ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-api/releases/tag/v0.4.3',
    license='BSD')
