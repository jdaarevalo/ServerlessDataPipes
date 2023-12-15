from setuptools import setup, find_packages

setup(
    name='ServerlessDataPipes',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'serverlessdatapipes=serverlessdatapipes.cli.main:main',
        ],
    },
)
