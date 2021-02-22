import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)
    
    for j in x:
        print(j)

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

bubbleSort(arr)