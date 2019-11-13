from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.0.1'

if not version:
    raise RuntimeError('version is not set')

setup(name='python-module',
      author='Nobody',
      url='https://github.com/Isonami/draft_python_module',
      version=version,
      packages=find_packages(),
      license='MIT',
      entry_points={
        'console_scripts': ['show-some-magic=python_module:main'],
      }
      )
