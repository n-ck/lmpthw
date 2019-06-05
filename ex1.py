# Use:
# sys.argv
# Pythons argparse package

# Your test script should be able to handle the following situations:
# 1. Getting help with --help or -h
# 2. At least three arguments that are flags, meaning they don't take an extra argument but simply
# putting them on the command line turns something on.
# 3. At least three arguments that are options,meaning they do take an argument and set a variable in your script to that option.
# 4. Additional "positional" arguments, which are a list of files at the end of all the - style arguments and can handle Terminal wildcards like */.txt.

# Process:
# 1. Create new file
# 2. Copy in exercise summary
# 3. Research first command tool sys.arg
# 4. Added sys.argv example to script, tested in terminal until the output worked
# 5. Wrote & tested answer to first situation
# 6. Researched argv, switched research to the argparse package
# 7. Reading argparse documentation and trying (copy and pasting examples)
# 15-20 minutes so far
# 8. Research and implement arguments that are flags in argparse
# 9. Moved on to research and implementation of options arguments and positional arguments
# 10. Added help text to new args
# 11. Added all args without further script
# 20 min. progress

import sys
import argparse


## Using sys.argv
# print "This is the name of the script:", sys.argv[0]
# print "This is the first argument:", sys.argv[1]
# print "List of filename + arguments:", sys.argv

# if ("--help" in sys.argv) or ("-h" in sys.argv):
#     print "This is the help section"


## Using argparse:
parser = argparse.ArgumentParser(description='Creating a parser')

parser.add_argument('-w', action='store_true', help="flag 1") # flag argument
parser.add_argument('--boom', action='store_true', help="flag 2") # flag argument
parser.add_argument('-t', '--three', action='store_true', help="flag 3") # flag argument

parser.add_argument("-b", help="increase output verbosity") # optional argument
parser.add_argument('--foo', help='foo help') # optional argument
parser.add_argument("--verbosity", help="increase output verbosity") # optional argument

parser.add_argument("echo", help="echo the string you use here") # positional argument (required)
parser.add_argument("files", help="echo the string you use here") # positional argument (required)


args = parser.parse_args()

print args

print args.echo

print args.foo

