N = int(input())
arr = list(map(int, input().split()))

m = max(arr)
for index, i in enumerate(arr):
    arr[index] = i/m*100

print(sum(arr)/len(arr))
