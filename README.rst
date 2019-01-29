================
Sunday counter
================

This package provides a command to list Sundays between two dates.

This package is developed for python-3.6, so within this package, run::

   virtualenv -p $(which python3.6) .
   ./bin/python setup.py install

Now you can run::

   ./bin/countsundays -h

Example::

   ./bin/countsundays --start 1.1.1900 --end 1.2.1900

For reverse order::

   ./bin/countsundays --start 1.1.1900 --end 1.2.1900 --reverse

To print on file::

   ./bin/countsundays --start 1.1.1900 --end 1.2.1900 --reverse --path ~/sundays

* Printing to file append to the existing file.

Running the test::

   ./bin/python setup.py test
