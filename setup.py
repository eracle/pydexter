__author__ = 'Giacomo Berardi <barnets@gmail.com>'

from setuptools import setup, find_packages

readme_file='README.md'
def readme():
    with open(readme_file) as f:
        return f.read()

setup(name='pydexter',
      description='A Python client for the Dexter REST API',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords=['dexter', 'entity linking', 'wikification'],
      url='http://github.com/giacbrd/pydexter',
	)
