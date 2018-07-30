from setuptools import setup

setup(
    name='Highton',
    version='2.3.0',
    license='Apache License 2.0',
    description='A Python library for Highrise',
    long_description='A beautiful Python - Highrise - Wrapper.',
    url='https://github.com/seibert-media/Highton',
    author='Julia Giebelhausen, Jakob Löhnertz, Michael Bykovski',
    author_email='brogrammers@seibert-media.net',
    packages=[
        'highton',
        'highton.call_mixins',
        'highton.fields',
        'highton.models',
        'highton.parsing',
    ],
    install_requires=[
        'requests'
    ],
    keywords='seibertmedia seibert media python api wrapper highrise highton',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
