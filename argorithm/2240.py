import sys
input = sys.stdin.readline

T, W = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(T)]
temp = []

sum = 1
previous_num = arr[0]
for i in range(1, len(arr)):
    if previous_num == arr[i]:
        previous_num = arr[i]
        sum += 1
    else:
        previous_num = arr[i-1]
        temp.append(sum)
        sum = 0
print(temp)
