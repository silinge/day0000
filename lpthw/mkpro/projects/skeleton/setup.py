try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    'description':'Myproject',
    'author':'My name',
}

setup(**config)