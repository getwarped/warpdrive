import os

from setuptools import setup

def _files(prefix):
    result = []
    for root, dirs, files in os.walk(prefix, topdown=False):
        for name in files:
            if root == prefix:
                result.append(os.path.join(root[len(prefix):], name))
            else:
                result.append(os.path.join(root[len(prefix)+1:], name))
    return result

setup(name = 'warpdrive',
      version = '0.20.1',
      description = 'Launcher for Python web applications.',
      author = 'Graham Dumpleton',
      author_email = 'Graham.Dumpleton@gmail.com',
      license = 'BSD',
      url = 'https://github.com/GrahamDumpleton/warpdrive',
      packages = ['warpdrive', 'warpdrive.etc'],
      package_data = {'warpdrive.etc': _files('warpdrive/etc')},
      entry_points = {'console_scripts': ['warpdrive = warpdrive:main']},
     )
