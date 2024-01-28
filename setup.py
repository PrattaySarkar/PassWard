# PassWard/setup.py

from setuptools import setup, find_packages

setup(
    name='passward',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyperclip',
    ],
    entry_points={
        'console_scripts': [
            'passgen=passward.__main__:main',
        ],
    },
)
