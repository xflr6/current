# setup.py

from setuptools import setup

setup(
    name='current',
    version='0.3.3.dev0',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Current module relative paths and imports',
    keywords='sys.path import temporary inspect caller',
    license='CC0',
    url='https://github.com/xflr6/current',
    py_modules=['current'],
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    extras_require={
        'dev': ['flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['pytest>=3.3', 'pytest-cov'],
    },
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
