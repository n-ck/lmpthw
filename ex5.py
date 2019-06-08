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
        read_convert = str(open_file.read())
        if open_file.mode == "r":
            f.write(read_convert)
    f.close() 

else:
    for file in args.files:
        f = open(file, "r")
        if f.mode == 'r':
            print f.read()

if args.concat and args.n == True:
    with open(args.concat, "rw") as f:
        line = f.readline()
        count = 1
        while line:
            # print count, line
            line = line.strip()
            new_line = count, line
            f.write(new_line)
            count += 1



# 20 minutes read excercise & implemented basic cat functionality
# Implementing additional cat flags (from man cat manual)
# 25 minutes trying to implement line numbering