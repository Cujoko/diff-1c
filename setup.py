﻿# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup

here = Path(__file__).parent

about: Dict[str] = {}
with Path(here, 'diff_1c', '__about__.py').open() as f:
    exec(f.read(), about)

setup(
    name='diff_1c',
    version=about['__version__'],
    description='Diff utility for 1C:Enterprise',
    author='Cujoko',
    author_email='cujoko@gmail.com',
    url='https://gitlab.com/Cujoko/diff-1c',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    keywords='1c diff v8reader v8unpack gcomp',
    entry_points={
        'console_scripts': [
            'diff1c=diff_1c.__main__:run'
        ]
    },
    license='MIT',
    install_requires=[
        'commons @ https://gitlab.com/Cujoko/commons/-/archive/master/commons-master.tar.gz',
        'parse-1c-build @ https://gitlab.com/Cujoko/parse-1c-build/-/archive/master/parse-1c-build-master.tar.gz'
    ]
)
