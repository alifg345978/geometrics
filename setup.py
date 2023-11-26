from setuptools import setup, find_packages

setup(
    name='geometrics',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            # Define any command-line scripts here
        ],
    },
)
