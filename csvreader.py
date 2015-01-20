import argparse, csv

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=str)
parser.add_argument('output_file', type=str)
parser.add_argument('outlines', type=int)

args = parser.parse_args()
input_file = args.infile
output_file = args.output_file
outLines = args.outlines


with open(input_file, "rb") as my_file:
    reader = csv.reader(my_file)
    all_rows = list(reader)
    inLines = len(all_rows)
    if inLines < outLines:
        print "Ok, but the number of lines in file is less than the one you specified"
    write_file = output_file + "0"
    for i, row in enumerate(all_rows):
        with open(write_file, 'wb') as chunk:
            writer = csv.writer(chunk)
            writer.writerow(row)
            if i % outLines == 0:
                write_file = output_file + str(i / outLines)
                print write_file
