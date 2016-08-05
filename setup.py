#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
	name = 'pogotransfercalc',
	packages = ['pogotransfercalc'],
	version = '1.0.0',
	download_url = 'https://github.com/mathiasbynens/pogotransfercalc/tarball/v1.0.0',
	description = 'Easily calculate how many Pokémon you should transfer before kicking off an evolution spree in Pokémon GO',
	author = 'Mathias Bynens',
	author_email = 'mathias@qiwi.be',
	license='MIT',
	url = 'https://github.com/mathiasbynens/pogotransfercalc',
	keywords = ['pogo', 'pokemon go'],
	classifiers = [],
	test_suite='nose.collector',
	tests_require=['nose'],
)
