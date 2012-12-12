from setuptools import setup, find_packages
import sys, os

version = '0.0'

install_requires = ['SOAPPy', 'elementtree']

setup(name='LRSSpy',
      version=version,
      description="",
      long_description="""\
      """,
      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
