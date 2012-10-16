from paver.easy import *
from paver.setuputils import setup

import unittest
import subprocess

setup(
    name="AutoCupid",
    packages=['autocupid'],
    version="1.0",
    url="http://www.autocupid.us/",
    author="David Y. Kay",
    author_email="dk@autocupid.us"
)

@task
def test():
  """Run all tests."""
  loader = unittest.TestLoader()
  modules = loader.discover('.')
  unittest.TextTestRunner(verbosity=2).run(modules)

@task
def dev():
    result = subprocess.call(['python', './runserver.py'])

@task
def run():
  #script = """err=3
  #while test "$err" -eq 3 ; do
  #    python server.py
  #    err="$?"
  #done"""
  result = 3
  while result == 3:
    #subprocess.call(['./test.sh'])
    result = subprocess.call(['python', './main.py'])
  print "Ended with result: %d" % result
