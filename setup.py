''' package info '''
from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='langmaker',
    version='0.1.0',

    description='Instant language',
    url='https://github.com/mouse-reeve/langmaker',

    author='Mouse Reeve',
    author_email='mousereeve@riseup.net',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
    ],

    packages=['langmaker'],
    include_package_data=True,

    install_requires=['nltk', 'numpy']
)
