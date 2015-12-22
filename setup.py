# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='appload',
    version='0.0.1',
    author=u'José Manuel Sánchez',
    packages=['appload'],
    url='https://github.com/buscarini/appload',
    license='MIT licence, see LICENSE file',
    description='FTP upload',
    long_description=open('README.md').read(),
    zip_safe=False,
    scripts = ['scripts/appload.py'],
    install_requires = [
           'keyring'
     ]
)