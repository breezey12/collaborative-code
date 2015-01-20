import argparse, csv

parser = argparse.ArgumentParser()
parser.add_argument('i', type=str)
parser.add_argument('outfile', type=str)
parser.add_argument('numlines', type=int)

args = parser.parse_args()
input_file = args.i
outfile = args.outfile
numlines = args.numlines

print "number of lines is ", numlines

with open("state_table.csv", "rb") as my_file:
    reader = csv.reader(my_file)
    all_rows = list(reader)
    lines = len(all_rows)
    if lines < numlines:
        print "Ok, but the number of lines in file is less than the one you specified"
    write_file = outfile + "0"
    for i, row in enumerate(all_rows):
        with open(write_file, 'wb') as chunk:
            writer = csv.writer(chunk)
            writer.writerows(','.join(row))
            if i % numlines == 0:
                write_file = outfile + str(i / numlines)
