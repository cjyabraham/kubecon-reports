from setuptools import setup, find_packages

# https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration
setup(
    name='genreport',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas'
    ],
    entry_points='''
        [console_scripts]
        genreport=reporting.cli:cli
    ''',
)
