# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = """
django-pipeline-compass-rubygem is a Compass compiler for django-pipeline using the original Compass Ruby Gem.
"""

setup(
    name='django-pipeline-compass-rubygem',
    version='0.1.8',
    description=description,
    long_description=open('README.rst').read(),
    author='Patrick Stadler',
    author_email='patrick.stadler@gmail.com',
    url='https://github.com/mila-labs/django-pipeline-compass',
    license='MIT License',
    platforms=['OS Independent'],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Utilities',
    ]
)
