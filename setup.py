import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'flask',
]

tests_require = requires + [
    'nose',
    'mock',
]

setup(name='Unfuddle2Jenkins',
      version='0.0',
      description='Unfuddle2Jenkins',
      long_description=README + '\n\n' + CHANGES,
      classifiers=["Programming Language :: Python"],
      author='Jakub Jaroszewski',
      author_email='jakub.jaroszewski@gmail.com',
      url='https://github.com/pierd/unfuddle2jenkins',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      install_requires=requires,
      tests_require=tests_require,
      )
