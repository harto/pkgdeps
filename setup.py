from os import popen
from setuptools import setup, find_packages
import re

package = 'pkgdeps'

version = popen('git describe --tags').read().strip()

with open('README.rst') as f:
    long_description = f.read()

setup(
    name=package,
    version=version,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pkgdeps = pkgdeps:main']
    },
    description="Explore dependencies of a Python package by parsing its imports.",
    long_description=long_description,
    license='MIT',
    keywords='python package dependency',
    author='Stuart Campbell',
    author_email='stuart@harto.org',
    url='https://github.com/harto/pkgdeps',
)
