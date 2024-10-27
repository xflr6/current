import pathlib
from setuptools import setup

setup(
    name='current',
    version='0.4.2.dev0',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Current module relative paths and imports',
    keywords='sys.path import temporary inspect caller',
    license='CC0',
    url='https://github.com/xflr6/current',
    project_urls={
        'Issue Tracker': 'https://github.com/xflr6/current/issues',
        'CI': 'https://github.com/xflr6/current/actions',
        'Coverage': 'https://codecov.io/gh/xflr6/current',
    },
    py_modules=['current'],
    platforms='any',
    python_requires='>=3.9',
    extras_require={
        'dev': ['tox>=3', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['pytest>=7', 'pytest-cov'],
    },
    long_description=pathlib.Path('README.rst').read_text(encoding='utf-8'),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
