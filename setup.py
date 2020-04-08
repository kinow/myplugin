# plugins must be properly installed, in-place PYTHONPATH meddling will
# not work.
from setuptools import setup

setup(
    name='my-plugin',
    version='1.0',
    py_modules=['my_plugin'],
    entry_points={
       # register this plugin with Cylc
       'main_loop': [
         # name = python.namespace.of.module
         'my_plugin=my_plugin'
       ]
    }
)
