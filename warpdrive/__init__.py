from __future__ import print_function

version = '0.14.0'

import os
import sys

rootdir = os.path.dirname(__file__)
bindir = os.path.join(rootdir, 'bin')

def main(*args):
    args = sys.argv

    # Skip program name.

    action = args[1]
    args = args[2:]

    program = 'warpdrive-%s' % action
    executable = os.path.join(bindir, program)

    print(program, executable)

    os.environ['WARPDRIVE_VERSION'] = version

    os.execl(executable, program, *args)
