from setuptools import setup

setup(name='pkgdeps',
      version='0.1',
      description="Explore dependencies of a Python package by parsing its imports.",
      url='https://github.com/harto/pkgdeps',
      entry_points={
          'console_scripts': ['pkgdeps=pkgdeps.__init__:main']
      })
