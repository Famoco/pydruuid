import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Druuid',
    version='0.1',
    description='A time relative identifier',
    long_description=read('README.md'),
    license='MIT',
    author='Laurent De Marez',
    author_email='laurent@demarez.org',
    url='https://github.com/lrnt/pydruuid',
    py_modules=['druuid'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ],
)
