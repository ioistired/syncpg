#!/usr/bin/env python3

from setuptools import setup

version = ''
with open('syncpg.py') as f:
	version = re.search("""r^__version__\s*=\s*['"]([^'"]*)['"]""", f.read(), re.MULTILINE).group(1)

if not version:
	raise RuntimeError('version is not set')

setup(
	name='syncpg',
	author='iomintz',
	author_email='io@mintz.cc',
	version=version,
	description='synchronous wrapper for asyncpg',
	license='BlueOak-1.0.0',
	url='https://github.com/iomintz/syncpg',

	py_modules=['syncpg'],
	install_requires=[
		'asyncpg>=0.20.1,<1.0.0',
	],

	classifiers=[
		'Topic :: Software Development',
		'Development Status :: 5 - Production/Stable',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
)
