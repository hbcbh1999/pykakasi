#!/usr/bin/python
# derivered from unihandecode setup.py

from setuptools import Command,setup

import unittest
import os
import genkanwadict

UNITTESTS = [
        "tests", 
    ]

class TestCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        suite = unittest.TestSuite()

        suite.addTests( 
            unittest.defaultTestLoader.loadTestsFromNames( 
                                UNITTESTS ) )

        result = unittest.TextTestRunner(verbosity=2).run(suite)
class GenKanwa(Command):
    user_options = [ ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        src = os.path.join('data','kakasidict.utf8')        
        dst = os.path.join('unihandecode','kanwadict2.db')
        try:
            os.unlink(dst)
        except:
            pass
        kanwa = genkanwadict.mkkanwa()
        kanwa.run(src, dst)
        src = os.path.join('data','itaijidict.utf8')
        dst = os.path.join('unihandecode','itaijidict2.pickle')
        try:
            os.unlink(dst)
        except:
            pass
        kanwa.mkitaiji(src, dst)

setup(name='pykakasi',
      version='0.01',
      description='',
      url='http://launchpad.net/miurahr/+junk/pykakasi',
      license='GPLv3',
      long_description="",
      author='Hioshi Miura',
      author_email='miurahr@linux.com',

      packages = [ 'pykakasi' ],

      provides = [ 'pykakasi' ],

      cmdclass = { 'test': TestCommand, 'genkanwa':GenKanwa }
)