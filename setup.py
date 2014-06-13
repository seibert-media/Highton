import os
from setuptools import setup
 

# Allow setup.py to be run from any path
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
setup(
    name = 'Highton-API',
    version = '1.0.1',
    license = 'Apache License 2.0',
    description = 'A Python library for Highrise',
    long_description = read('README.md'),
    url = 'https://github.com/bykof/Highton-API',
    author = 'Michael Bykovski',
    author_email = 'bykof@me.com',
    py_modules=['Highton-API'],
    install_requires = ['requests', 'lxml'],
    keywords = 'bykof python api highrise highton',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)