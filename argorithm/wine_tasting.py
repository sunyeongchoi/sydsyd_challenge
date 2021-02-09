import sys
input = sys.stdin.readline

n = int(input())
arr = list(int(input().rstrip()) for _ in range(n))

answer = []
for i in range(2):
    sum = 0
    for index, j in enumerate(arr):
        if (i+index)%3==0:
            continue
        sum += j
    answer.append(sum)
print(max(answer))