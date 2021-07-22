#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxStreaks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY toss as parameter.
#

def getMaxStreaks(toss):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    print(toss)
    toss.append("hello")
    mhead=0
    mtail=0
    hCount=0
    tCount=0
    for i in range(len(toss)-1):
            if toss[i]=="Heads":
                while(toss[i]=="Heads"):
                    hCount=hCount+1
                    i=i+1
                if(hCount>=mhead):
                    mhead=hCount
                hCount=0
                tCount=0
            if toss[i]=="Tails":
                while(toss[i]=="Tails"):
                    tCount=tCount+1
                    i=i+1
                if(tCount>=mtail):
                    mtail=tCount
                hCount=0
                tCount=0
        
        
#         if toss[i]=="Heads":
#             hCount=hCount+1
#             if (toss[i+1]=="Tails" or toss[i+1]=="hello") and hCount>=mhead:
#                 mhead=hCount
#                 hCount=0
#                 tCount=0
#         elif toss[i]=="Tails":
#             tCount=tCount+1
#             if (toss[i+1]=="Heads" or toss[i+1]=="hello") and tCount>=mtail:
#                 mtail=tCount
#                 tCount=0
#                 hCount=0
    return [mhead,mtail]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    toss_count = int(input().strip())

    toss = []

    for _ in range(toss_count):
        toss_item = input()
        toss.append(toss_item)

    ans = getMaxStreaks(toss)

    fptr.write(' '.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
