from distutils.core import setup

setup(
    name='keras-utilities',
    version='0.1dev',
    packages=['keras_utilities',],
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
