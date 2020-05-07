#!/usr/bin/env python3

import re
from setuptools import setup

with open('README.md') as f:
	long_description = f.read()

version = ''
with open('syncpg.py') as f:
	m = re.search(r"""^__version__\s*=\s*['"]([^'"]*)['"]""", f.read(), re.MULTILINE)
	if m:
		version = m.group(1)

if not version:
	raise RuntimeError('version is not set')

setup(
	name='syncpg',
	author='iomintz',
	author_email='io@mintz.cc',
	version=version,
	description='synchronous wrapper for asyncpg',
	long_description=long_description,
	long_description_content_type='text/markdown',
	license='BlueOak-1.0.0',
	url='https://github.com/iomintz/syncpg',

	py_modules=['syncpg'],
	install_requires=[
		'asyncpg>=0.20.1,<1.0.0',
	],

	classifiers=[
		'Topic :: Software Development',
		'Topic :: Database :: Front-Ends',
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
)
