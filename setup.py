from setuptools import setup, find_packages

setup(
    name='Sales_Data_Analysis',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'pytest',
        'pylint',
    ],
    entry_points={
        'console_scripts': [
            'Sales_Data_Analysis=main:main',
        ],
    },
)
