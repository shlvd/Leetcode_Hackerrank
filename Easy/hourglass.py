import math
import os
import random
import re
import sys


def hourglassSum(arr):
    total = 0
    max_total = -7 * 9 - 1
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_total = max(max_total, total)
    return max_total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
