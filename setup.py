try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Analysis of movie data',
    'author': 'Mariana Souza',
    'url': '',
    'download_url': 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films',
    'author_email': 'xxxx@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': ['getMovieData.py', 'VisualizingMovie.py'],
    'name': 'analysis-Academy-Award-winning-films'
}

setup(**config)