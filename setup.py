import os
from setuptools import setup
 
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'Highton-API',
    version = '0.1',
    license = 'Apache License 2.0',
    description = 'A Python library for Highrise',
    long_description = README,
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
        'License :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)