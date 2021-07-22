

import math
import os
import random
import re
import sys
import string


#Complete the 'getStrength' function below.
#The function is expected to return an INTEGER.
#The function accepts following parameters:
#1. STRING password
#2. INTEGER weight_a


def getStrength(password, weight_a):
    # Complete the function
    alpha_list = list(map(chr, range(97, 123)))
    for i in range(0,weight_a): 
        alpha_list.insert(0, alpha_list.pop()) 
    res=0
    for i in password:
        res=res+alpha_list.index(i)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    password = input()
    weight_a = int(input().strip())
    strength = getStrength(password, weight_a)
    fptr.write(str(strength) + '\n')
    fptr.close()
