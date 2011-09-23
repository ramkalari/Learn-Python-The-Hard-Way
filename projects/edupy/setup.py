try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Tips & Tricks',
    'author': 'Sriram Balasubramanian',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ramkalari@gmail.com',
    'version': 0.1,
    'install_requires': ['nose'],
    'packages': ['edu_decorators'],
    'scripts': ['edu_decorators/edu_dec.py'],
    'name': 'edupy'
}

setup(**config)
