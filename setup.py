from setuptools import setup, find_packages
import sys, os

version = '0.4.1'

setup(
	name='ckanext-odpat',
	version=version,
	description="Backend-Extension for opendataportal.at",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Michael Reichart',
	author_email='michael.reichart@brz.gv.at',
	url='brz.gv.at',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.odpat'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
		odpat=ckanext.odpat.plugin:OdpatPortalPlugin
	""",
)
