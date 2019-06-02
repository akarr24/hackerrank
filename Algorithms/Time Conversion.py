#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.strip()
    hh = time[0:2]
    period = time[-2:]

    if period == 'AM':
        if hh == '12':
            output = '00' + time[2:-2]
        else:
            output = time[0:-2]
    elif period == 'PM':
        hh = time[0:2]
        if hh == '12':
            output = time[0:-2]
        else:
            output = str(int(hh) + 12) + time[2:-2]
    else:
        assert False

    return output


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
