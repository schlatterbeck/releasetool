#!/usr/bin/python3

from rsclib.Freshmeat import Freshmeat, Release
from optparse         import OptionParser

usage  = "%proc [options] project changenote-file version"
parser = OptionParser (usage = usage)
parser.add_option \
    ( "-t", "--tag"
    , dest    = "tag"
    , action  = "append"
    , help    = "Tag for release (may be specified more than once)"
    , default = []
    )
(opt, args) = parser.parse_args ()
if len (args) != 3 :
    parser.error ("Need three arguments")
    sys.exit (23)

changelog = open (args [1], 'r').read ()
r  = Release   (args [2], changelog, False, *opt.tag)
fm = Freshmeat (args [0], 'releases', put = r)
if fm.code :
    print (fm.code, fm.result)
    print (fm.err)
else :
    print (fm.pretty ())
fm = Freshmeat (args [0], 'releases/pending')
print (fm.pretty ())
