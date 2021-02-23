import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = mergeSort(array[:mid])
    print('left : ', left)
    right = mergeSort(array[mid:])
    print('right : ', right)

    i, j, k = 0, 0, 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1
    
    if i==len(left):
        while j<len(right):
            array[k] = right[j]
            j+=1
            k+=1
    elif j==len(right):
        while i<len(left):
            array[k] = left[i]
            i+=1
            k+=1
    return array

answer = mergeSort(arr)
for i in answer:
    print(i)