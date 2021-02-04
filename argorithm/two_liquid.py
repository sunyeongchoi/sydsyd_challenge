import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

min = sys.maxsize
answer = 0
for a in arr:
    for b in arr:
        if a+b < min:
            min = abs(a+b)
            answer = a, b
for i in sorted(answer):
    print(i, end=' ')
