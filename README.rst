pkgdeps
=======

Explore dependencies of a Python package by parsing its imports.

This might be useful for:

- seeing how modules within a package depend on each other
- seeing which built-in libraries are relied upon
- analysis of 3rd-party dependencies
- etc.


Examples
--------

Explore dependencies of this project::

    $ pkgdeps /path/to/pkgdeps
    pkgdeps
      - argparse.ArgumentParser
      - ast
      - collections.defaultdict
      - functools.reduce
      - os
      - os.path
      - sys


Limitations
-----------

- Only tested with Python 3 against Python 3 packages.
- Doesn't handle conditional imports; all conditional branches are inspected.
- Outputs imported module members: ``from os.path import join`` creates a
  dependency on ``os.path.join``, but we probably only want ``os.path`` for e.g.
  ``tsort`` output. However, internal dependencies are coarsened to the module
  level.


Installation
------------

::

    $ pip install pkgdeps


Usage
-----

Various options are available to filter and format the output::

    $ pkgdeps -h
    usage: pkgdeps [-h] [-n <num>] [-m <num>] [-e <type> | -o <type>]
                   [-f <format>]
                   </path/to/package>

    Explore dependencies of a package by parsing its imports.

    positional arguments:
      </path/to/package>    path to package root

    optional arguments:
      -h, --help            show this help message and exit
      -n <num>, --package-module-name-segments <num>
                            truncate module names of inspected package to given
                            number of segments (and consolidate imports)
      -m <num>, --dependency-module-name-segments <num>
                            truncate module names of dependencies to given number
                            of segments (and deduplicate)
      -e <type>, --exclude <type>
                            exclude various kinds of dependencies from output
                            (builtin, 3rd-party, internal)
      -o <type>, --only <type>
                            include only dependencies of the given type (builtin,
                            3rd-party, internal)
      -f <format>, --format <format>
                            graph output format (tree, tsort)
