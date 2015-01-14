import argparse
parser = argparse.ArgumentParser()
parser.add_argument('endingNumber',type=int,help="this is the last number that'll be counted")
parser.add_argument('startingNumber',type=int)
parser.add_argument('-even',action="store_true",help="display only even numbers")
args = parser.parse_args()

end = args.endingNumber
start = args.startingNumber
even = args.even

def counting(a,z):
	for i in xrange(a,z+1):
		if even:
			if i % 2 == 0:
				print i
		else:
			print i

if __name__ == "__main__":
	counting(start,end)
