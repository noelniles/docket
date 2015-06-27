"""
Copyright 2015 Noel Niles
explore.py is part of Docket.

    Docket is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Docket is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Docket.  If not, see <http://www.gnu.org/licenses/>.
"""
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
