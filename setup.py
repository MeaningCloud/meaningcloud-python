#! /usr/bin/env python


# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    
    name='MeaningCloud-python',  

   
    version='1.0.0',  

   
    description='Official Python SDK for MeaningCloud API', 

    
    url='https://gitlab.com/meaningcloud/public/meaningcloud-python', 

   
    author='MeaningCloud',  

    
    author_email='support@meaningcloud.com',


   
    keywords='nlp, MeaningCloud, text analytics', 

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  

   
    install_requires=[
	'requests'
	
	], 

    
    extras_require={  
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

)
