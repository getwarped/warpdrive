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

long_description = open('README.rst').read()

classifiers = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
]

setup(name = 'warpdrive',
      version = '0.26.4',
      description = 'Launcher for Python web applications.',
      long_description=long_description,
      url = 'https://github.com/GrahamDumpleton/warpdrive',
      author = 'Graham Dumpleton',
      author_email = 'Graham.Dumpleton@gmail.com',
      license = 'BSD',
      classifiers = classifiers,
      keywords='wgsi docker openshift',
      packages = ['warpdrive', 'warpdrive.etc'],
      package_data = {'warpdrive.etc': _files('warpdrive/etc')},
      entry_points = {'console_scripts': ['warpdrive = warpdrive:main']},
     )
