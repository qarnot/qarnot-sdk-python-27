#!/usr/bin/env python
"""Setuptools file."""

# pylint: disable=E0611,F0401
from setuptools import setup
from os import path
import io
import versioneer

try:
    import setuptools
    [setuptools]
except ImportError:
    pass

with io.open(path.join(path.dirname(__file__), 'README.rst'), encoding="utf-8") as long_d_f:
    LONG_DESCRIPTION = long_d_f.read()

setup(name='qarnot',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Qarnot Computing SDK',
      long_description=LONG_DESCRIPTION,
      author='Qarnot computing',
      author_email='support@qarnot-computing.com',
      url='https://computing.qarnot.com',
      setup_requires=['setuptools<45', 'wheel<0.38'],
      packages=['qarnot'],
      install_requires=['requests<2.28', 'boto3>=1.9,<=1.17.112', 'wheel<0.38', 'deprecation', 'simplejson'],
      tests_require=['pytest<5'],
      python_requires='>=2.7',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Information Technology',
                   'License :: OSI Approved :: Apache Software License'],
      license='apache')
