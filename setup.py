from setuptools import find_packages
from setuptools import setup


setup(
    name='import_finder',
    version='0.1.0',
    description='Quick regex tool for finding directly imported packages',
    author='Michael Christen',
    url='https://github.com/michael-christen/import-finder',
    license='MIT',
    packages=find_packages(exclude=["*.tests"]),
    install_requires=[
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'import_finder=import_finder.import_finder:find',
        ],
    },
)
