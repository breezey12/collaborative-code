from sys import argv


def count(start, end, incrementBy=1):
    # enumerates between start and end, only lists even numbers if even = true
    while start <= end:
        print start
        start += incrementBy


def even(start):
    start += start % 2
    incrementBy = 2
    return start, incrementBy

def countBy(countByVal):
    incrementBy = countByVal
    return incrementBy


if __name__ == "__main__":
    """ validates the number of arguments, enumerates positional arguments,
    finds and stores optional arguments, then feeds them all to count()
    """
    paramct = len(argv)-1
    optional_args = []
    ordered_args = []
    if paramct < 2:
        print "At least two arguments are required."
    else:
        for arg in argv:
            if arg[0] == "-":
                optional_args.append(arg[1:])
            else:
                ordered_args.append(arg)
                start = int(arg)
                end = int(argv[2])
        count(start, end)