import sys
import multiprocessing
import os
from random import randint

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:   
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def mergeSort(pipe, arr):
    if len(arr) < 2:
        pipe.send(arr)
    else:
        middle = len(arr)//2
        a, b = multiprocessing.Pipe()
        l = multiprocessing.Process(target=mergeSort, args=(b, arr[:middle]))
        r = multiprocessing.Process(target=mergeSort, args=(b, arr[middle:]))
        l.start()
        r.start()
        left = a.recv()
        right = a.recv()
        l.join()
        r.join()
        pipe.send(merge(left, right))

def main():
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        N = 8
    aList = [randint(1, N*N) for i in range(N)]
    print(aList)
    a, b = multiprocessing.Pipe()
    p = multiprocessing.Process(target=mergeSort, args=(b, aList))
    p.start()
    print(a.recv())
    p.join()

main()
