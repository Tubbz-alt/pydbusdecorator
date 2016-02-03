#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''

from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='pydbusdecorator',
      version='2.0',
      description='Python decorator for dbus interface clients',
      author='Antergos Developers',
      author_email='dev@antergos.com',
      url='https://github.com/antergos/pydbusdecorator',
      keywords = ["dbus"],
      packages=('dbusdecorator',),
      requires=(),
      license = "GPL",
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5"
      ],
      long_description = readme
)
