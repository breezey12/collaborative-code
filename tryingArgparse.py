def evenF(number):
    if number % 2 == 0:
        return number


def countByF(start, number):
    if (number-start) % countBy == 0:
        return number
    else:
        return 0


def counting(a, z):
    for i in xrange(a, z+1):
        if even and countBy:
            result = countByF(a, i)
            result = evenF(result)
        elif even:
            result = evenF(i)
        elif countBy:
            result = countByF(a, i)
        else:
            result = i
        if result == 0 or result is None:
                continue
        else:
            print result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('startingNumber', type=int)
    parser.add_argument('endingNumber', type=int, help="this is the last number \
    that'll be counted")
    parser.add_argument('-even', action="store_true", help="display only even \
    numbers")
    parser.add_argument('-countby', type=int)
    args = parser.parse_args()
    end = args.endingNumber
    start = args.startingNumber
    even = args.even
    countBy = args.countby
    counting(start, end)
