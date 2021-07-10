#!/bin/sh
echo "Read-me, not execute-me. Usage:"
echo "  cat transpile-python-to-javascript.sh"
exit

# NOTE: transpile-python-to-javascript.sh file is just a general test.
#       But in general, like most programming languages transpilers, the
#       averange case (like loops, constructs, etc) are easy to port, but
#       external complex dependencies, like IO manipulation, are not
#       automatically ported.
#
#       Also, even if parts of the HXLm could be ported to JavaScript (and the
#       code could run on browser or server with NodeJS) the end code would
#       still not as beauty as if an human do by hand on JavaScript. But parts
#       of HXLm, maybe the ones related to HXLm.lisp, we could do some work
#       to see if even an ugly code could be transpiled directly from HXLm to
#       something that could run.


#### Generate hxlm/ontologia/javascript files _________________________________
# Using metapensiero.pj, this will generate the files
pj --output hxlm/ontologia/javascript hxlm/ontologia/python/

# Note: it generate all files from hxlm/ontologia/python/, including the
#       classes, but at the moment only hxlm_bootstrapping.py is not
#       removed from commit on git history.


#### metapensiero/metapensiero.pj test ________________________________________
# @see https://github.com/metapensiero/metapensiero.pj

pip3 install javascripthon

# This will not generate error:
pj hxlm/ontologia/python/hdp/radix.py

# This, as expected, will generate error on very specific python usages, like
# the '@lru_cache(maxsize=128)' (used for cache, but this could be ignored
# and, as somewhat expected, the 'with open(norm_path, 'r') as stream:'
# (file system manipulation)
pj hxlm/core/io/local.py


#### QQuick/Transcrypt test ____________________________________________________
# @see https://github.com/QQuick/Transcrypt
# @see http://www.transcrypt.org/#hello

# Note: not tested with Transcrypt