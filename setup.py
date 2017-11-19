from setuptools import setup

setup(
    name='pymschap',
    version='0.1',
    packages=['pymschap'],
    url='https://github.com/talkincode/pymschap',
    license='LGPL',
    author='jamiesun',
    author_email='jamiesun.net@gmail.com',
    description='python mschap module', long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 6 - Mature', 'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7', 'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['mschap','mschapv1', 'mschapv2','pymschap'],
)
