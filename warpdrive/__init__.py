from __future__ import print_function

version = '0.20.1'

import os
import sys

root = os.path.dirname(__file__)
scripts = os.path.join(root, 'etc')

def main(*args):
    args = sys.argv

    # Skip program name.

    action = args[1]
    args = args[2:]

    program = 'warpdrive-%s' % action
    executable = os.path.join(scripts, program)

    os.environ['WARPDRIVE_VERSION'] = version

    os.execl(executable, program, *args)
