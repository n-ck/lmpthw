import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", help="filename - required positional argument")
parser.add_argument("-concat", help="filename of new file for concatanation")
parser.add_argument("-n", action='store_true', help="Number the output lines, starting at 1")
args = parser.parse_args()

print args


if args.concat:
    f = open(args.concat,"a+")
    for file in args.files:
        open_file = open(file, "r")
        read_convert = str(o.read())
        if open_file.mode == "r":
            f.write(read_convert)
    f.close() 

else:
    for file in args.files:
        f = open(file, "r")
        if f.mode == 'r':
            print f.read()


# 20 minutes read excercise & implemented basic cat functionality
# Implementing additional cat flags (from man cat manual)