import argparse
import glob
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="directory to search in") # positional argument
parser.add_argument("-name", help="name to search, pattern match")
parser.add_argument("-type", help="type of the searched pattern")
parser.add_argument("-print", help="print the search results")

args = parser.parse_args()

subprocess.call(['pwd', 'ls', '-1'], shell=True)
subprocess.call('echo $HOME', shell=True)

print args.directory

print args.name

# type_list = ['b', 'c', 'd', 'f', 'l', 'p', 's']
type_list = ['d', 'f']

# print glob.glob("~")

if args.name:
    print args.name

if args.type:
    if args.type == 'd':
        print "directory"
    elif args.type == 'f':
        print "file"


# sudo code: 
# - positional argument for the directory path/name
# - -name argument with the search phrase
# - -type arugment to filter by file typ (file or directory)
# - -print to print the search results (if any)


# 45 minutes into the exercise including research
#

# Exercise / General format of find:
# 1. The directory to start searching in: . or /usr/local/.
# 2. A filter argument like -name or -type d(files of type directory). 
# 3. An action to do with each found file: -print.


# Implement the following flags for this exercise:

# -name
# True if the last component of the pathname being examined matches pattern.
# Special shell pattern matching characters (``['', ``]'', ``*'', and ``?'')
# may be used as part of pattern.  These characters may be matched explicitly
# by escaping them with a backslash (``\'').

# -type
# True if the file is of the specified type.  Possible file types are as fol-
# lows:

# b       block special
# c       character special
# d       directory
# f       regular file
# l       symbolic link
# p       FIFO
# s       socket


# -print
# This primary always evaluates to true.  It prints the pathname of the current file to standard output.

# -exec ## save for last, challenging
# True if the program named utility returns a zero value as its exit status.
# Optional arguments may be passed to the utility.  The expression must be
# terminated by a semicolon (``;'').  If you invoke find from a shell you may
# need to quote the semicolon if the shell would otherwise treat it as a con-
# trol operator.  If the string ``{}'' appears anywhere in the utility name or
# the arguments it is replaced by the pathname of the current file.  Utility
# will be executed from the directory from which find was executed.  Utility
# and arguments are not subject to the further expansion of shell patterns and
# constructs.
