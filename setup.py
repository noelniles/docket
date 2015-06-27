try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Explore law dockets',
    'author': 'Noel Niles',
    'url': 'https://github.com/shakabra/docket',
    'download_url': 'https://github.com/shakabra/docket',
    'author_email': 'noelniles@gmail.com',
    'version': '0.0.0.1',
    'install_requires': ['nose'],
    'packages': ['docket'],
    'scripts': [],
    'name': 'docket'
}

setup(**config)
