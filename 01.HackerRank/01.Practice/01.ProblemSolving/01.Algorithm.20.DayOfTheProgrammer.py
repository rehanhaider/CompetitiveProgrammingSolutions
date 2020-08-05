#Link to the question below
#

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    day = str()
    if year<1918:
        if year%4==0:
            day = "12.09."+str(year)
        else:
            day = "13.09."+str(year)
    elif year>1918:
        if year%400==0 or (year%4==0 and year%100 != 0):
            day = "12.09."+str(year)
        else:
            day = "13.09."+str(year)
    else:
        day = "26.09."+str(year)

    return day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()