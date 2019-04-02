from setuptools import setup

setup(
    name="stocktracker",
    version='0.1',
    py_modules=['stocktracker'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        stocktracker=stocktracker:quote
    ''',
)