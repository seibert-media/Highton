from setuptools import setup

setup(
    name='Highton',
    version='2.0',
    license='Apache License 2.0',
    description='A Python library for Highrise',
    long_description='A beautiful Python - Highrise - API. Less is more.',
    url='https://github.com/seibert-media/Highton',
    author='Julia Giebelhausen, Jakob Löhnertz, Michael Bykovski',
    author_email='brogrammers@seibert-media.net',
    packages=['highton', 'highton.classes'],
    install_requires=[],
    keywords='seibertmedia seibert media python api wrapper highrise highton',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6.2',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
