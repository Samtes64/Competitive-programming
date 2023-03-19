import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    key = arr[-1]
    i = arr.index(key)
    j = i-1
    while key<arr[j]:
        arr[i]=arr[j]
        j-=1
        i-=1
        print(*arr)
        if i==0:
            break
    arr[i]=key
    print(*arr)
   

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
