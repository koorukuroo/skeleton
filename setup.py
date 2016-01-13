# -*- coding: utf8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'packages': ['NAME'],
    'description': 'My project',
    'author': 'Kyunghoon Kim',
    'url': 'http://core.today',
    'download_url': 'http://information.center',
    'author_email': 'preware@gmail.com',
    'version': '0.1',
    'install_requirements': ['nose'],
    'scripts': [],
    'name': 'project name',
    'include_pakcage_data': True,
    'package_data': {'': ['assets/*.txt']}
}

setup(**config)
