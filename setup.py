from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pymediamover',
    version='0.1',

    description='A Utility for Organizing Your Digital Media',
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],

    url='https://github.com/seancallaway/pyMediaMover',
    author='Sean Callaway',
    author_email='seancallaway@gmail.com',
    license='GPLv3',
    packages=['pymediamover'],

    entry_points={
        'console_scripts': [
            'pymediamover = pymediamover.script:cli'
        ],
    },
)
