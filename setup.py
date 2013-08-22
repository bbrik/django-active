# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import active


setup(
    name='django-active',
    version=active.__version__,
    url='https://github.com/bbrik/django-active.git',
    author=u'Bernardo Brik',
    author_email='bernardobrik@gmail.com',
    description='Tags for styling links as active',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
)
