# setup.py

import io
from setuptools import setup

setup(
    name='current',
    version='0.3.6',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Current module relative paths and imports',
    keywords='sys.path import temporary inspect caller',
    license='CC0',
    url='https://github.com/xflr6/current',
    py_modules=['current'],
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    extras_require={
        'dev': ['flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': [
            'pytest>=3.4,!=3.10.0',
            'pytest-cov',
            'pathlib2; python_version < "3"',
        ],
    },
    long_description=io.open('README.rst', encoding='utf-8').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
