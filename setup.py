#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


readme = open('README.md').read()
history = open('CHANGELOG.md').read()

setup(
    author='Anmol Chachra',
    author_email='anmol.chachra@gmail.com',
    name='django-location-app',
    version='1.0.1',
    install_requires=['Django>=3.0'],
    python_requires='>=3.7',
    keywords='django geocomplete google maps places',
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    description='A Django app that helps you easily manage your own location data with autocomplete function. Connect your app to a completely normalized location database, avoid redundant Google Map API queries and save your hard earned money.',
    license='MIT',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    url='https://github.com/AnmolChachra/django-location-app',
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'places': [
            'templates/location_app/*.html',
            'static/location_app/js/*.js',
        ],
    },
    project_urls={
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'https://saythanks.io/to/anmol.chachra@gmail.com',
        'Source': 'https://github.com/AnmolChachra/django-location-app/',
        'Tracker': 'https://github.com/AnmolChachra/django-location-app/issues',
    },
    zip_safe=False,
)