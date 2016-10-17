#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
	name = 'pogotransfercalc',
	packages = ['pogotransfercalc'],
	version = '1.0.2',
	download_url = 'https://github.com/mathiasbynens/pogotransfercalc/tarball/v1.0.2',
	description = 'Easily calculate how many Pokémon you should transfer before kicking off an evolution spree in Pokémon GO',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Software Development :: Libraries',
	],
	author = 'Mathias Bynens',
	author_email = 'mathias@qiwi.be',
	license='MIT',
	url = 'https://github.com/mathiasbynens/pogotransfercalc',
	keywords = ['pogo', 'pokemon go'],
	test_suite='nose.collector',
	tests_require=['nose'],
)
