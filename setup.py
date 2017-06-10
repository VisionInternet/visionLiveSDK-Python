# -*- coding: utf-8 -*-
##############################################################################
#
#    Python visionLive API
#    Copyright 2017 Vision Internet (http://www.visioninternet.com)
#
##############################################################################

from setuptools import setup, find_packages
import os
import re

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    init = read(os.path.join('visionLiveAPI', '__init__.py'))
    return re.search("__version__ = '([0-9.]*)'", init).group(1)

setup(name='python-visionLiveAPI',
    version=get_version(),
    description='Library for visionLive api ',
    long_description=read('README.md'),
    author='Vision Internet',
    author_email='yding@visioninternet.com',
    url='https://github.com/VisionInternet/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    license='AGPLv3+',
    use_2to3=True,
    )