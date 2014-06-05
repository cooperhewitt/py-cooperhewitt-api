#!/usr/bin/env python

from distutils.core import setup

setup(name='cooperhewitt-api',
      version='0.1',
      description='Simple Python wrapper for Cooper-Hewitt API',
      author='Smithsonian Cooper-Hewitt National Design Museum',
      url='https://github.com/cooperhewitt/py-cooperhewitt-api',
      requires=[],
      packages=[
          'cooperhewitt',
          'cooperhewitt.api'
      ],
      scripts=[],
      download_url='https://github.com/cooperhewitt/py-cooperhewitt-api/releases/tag/v0.1',
      license='BSD')
