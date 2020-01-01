from setuptools import setup

setup(
   name='Autocorrect',
   version='1.0',
   description='Implements The Autocorrect Function',
   author='Ibrahim Ipek',
   author_email='ibrahimipek0218@gmail.com',
   packages=['Autocorrect'],  
   install_requires=['python-Levenshtein', 'wordfreq']
)
