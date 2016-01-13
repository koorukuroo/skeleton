# -*- coding: utf8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My project',
    'author': 'Kyunghoon Kim',
    'url': 'http://core.today',
    'download_url': 'http://information.center',
    'author_email': 'preware@gmail.com',
    'version': '0.1',
    'install_requirements': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project name'
}

setup(**config)