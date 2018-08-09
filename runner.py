#! /usr/bin/env python
""" Used in PyCharm IDE; should be in root of PyCharm project directory structure. """
import os

from web import create_app
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

# Flask Manager is a wrapper for argparse
from flask_script import Manager

app = create_app('dev')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
