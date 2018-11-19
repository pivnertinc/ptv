#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def reqs():
    with open('requirements.txt') as f:
        return f.read()

setup(name='pillage',
      packages=['pillage'],
      install_requires=reqs())
