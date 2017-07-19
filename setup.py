from setuptools import setup, find_packages

setup(
    name='keras-utilities',
    version='0.1dev',
    packages=find_packages(),
    install_requires=[
        'bcolz',
        'matplotlib',
        'numpy',
        'scipy',
        'scikit-learn',
        'keras==1.2.2',
        'theano'
    ],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read()
)
