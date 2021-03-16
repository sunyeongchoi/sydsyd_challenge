import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))


answer = 0
for index, i in enumerate(arr):
    answer += sum(arr[:index+1])
print(answer)

