''' Sample test module

    This test module performs tests on the modules in \sample directory

    The only correct way to call this module from the command line is to:

    a) Position yourself in the top project directory (e.g. 'Sample'),
       i.e. the one above the tests directory

    b) And to issue the command python -m tests.test_basic

'''

#
# The following two lines are necessary for the -m switch to function properly
# The -m switch launches the script by module name, rather than file name
# But unless the 'patch' below is included the package name is unknown
# For details read PEP 366: https://www.python.org/dev/peps/pep-0366/
#
if __name__ == "__main__" and __package__ is None:
    __package__ = "test_basic"

#
# Next you need the context.py file in the tests directory, as is described
# in this paper: https://docs.python-guide.org/writing/structure/
# But the first line only gives access to the directory (or rather package,
# because the directory contains a __init__.py file
# Afterwards you still need to import the actual module ('helpers')
#
from .context import sample
import sample.helpers as helpers

#
# Finally, this is the actual test
# So, your test code goes here
#
if "world" in helpers.message():
    print "OK"
else:
    print "Not OK"
