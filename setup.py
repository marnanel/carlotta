#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='Entropy of Carlotta',
		version='0.1',
		description='Mailing list system',
		author='Marnanel Thurman, Lars Wirzenius',
		author_email='marnanel@thurman.org.uk',
		url='https://github.com/tthurman/carlotta',
		packages=find_packages(),
                package_data={
                        'carlotta': ['templates/*'],
                },
		scripts=[
                        'scripts/carlotta'
                        ],
		install_requires=[
		        ],
                setup_requires = [
                        "setuptools_git >= 0.3",
                        ],
     )
