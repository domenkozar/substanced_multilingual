# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='substanced_multilingual',
    version='0.1.dev0',
    description='Multilingual support for Substance D',
    long_description=read('README.rst') +
                     read('HISTORY.rst'),
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    keywords='web wsgi pylons pyramid',
    author='Domen Kožar',
    author_email='domen@dev.si',
    url='https://substanced_multilingual.readthedocs.org/',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'substanced',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'coverage',
            'unittest2',
            'flake8',
        ],
        'development': [
            'zest.releaser',
            'Sphinx',
        ],
    },
    entry_points="""
    [paste.app_factory]

    [console_scripts]
    """,
    paster_plugins=['pyramid'],
    include_package_data=True,
    zip_safe=False,
)
