try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'description': '',
    'author': 'Forrest Alvarez',
    'url': 'https://github.com/gravyboat/ididthis',
    'version': '0.1',
    'install_requires': ['nose', 'pyyaml', 'Click'],
    'packages': ['ididthis'],
    'scripts': [],
    'name': 'ididthis'
}

setup(**config)
