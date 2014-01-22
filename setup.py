# setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='current',
    version='0.2',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Current module relative paths and imports',
    license='CC0',
    keywords='sys.path import temporary inspect caller',
    url='http://github.com/xflr6/current',
    py_modules=['current'],
    platforms='any',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
