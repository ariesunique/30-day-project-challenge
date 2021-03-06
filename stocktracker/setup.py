from setuptools import setup

setup(
    name="stocktracker",
    version='0.1',
    py_modules=['stocktracker'],
    install_requires=[
        'Click',
        'requests',
    ],
    data_files=[('', ['config.ini'])],
    entry_points='''
        [console_scripts]
        stocktracker=stocktracker:quote
    ''',
)