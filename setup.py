try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Python Project Skeleton',
	'author': 'Alan Tibbetts',
	'url': 'https://github.com/blackenedsystems',
	'download_url': 'https://github.com/blackenedsystems',
	'author_email': 'alan@blackenedsystems.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)