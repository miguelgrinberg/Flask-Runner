"""
Flask-Runner
------------

A set of standard command line arguments for Flask applications
"""
from setuptools import setup


setup(
    name='Flask-Runner',
    version='2.1.1',
    url='http://github.com/miguelgrinberg/flask-runner/',
    license='BSD',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description='A set of standard command line arguments for Flask applications built on top of Flask-Script',
    long_description=__doc__,
    py_modules=['flask_runner'],
    zip_safe=False,
    data_files=[('', ['README.md', 'LICENSE'])],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.9,<0.11',
        'Flask-Script>=0.6,<0.7',
        'argparse',
        'nose'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

