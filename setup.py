#! /usr/bin/env python

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    
    name='MeaningCloud-python',  

   
    version='1.0.3',

   
    description='Official Python SDK for MeaningCloud API',

    
    url='https://github.com/MeaningCloud/meaningcloud-python', 

   
    author='MeaningCloud',  

    
    author_email='support@meaningcloud.com',


   
    keywords='nlp, MeaningCloud, text analytics', 

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],

    
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  

   
    install_requires=[
	'requests[security]'
	],

    
    extras_require={  
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

)
