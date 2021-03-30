import sys; input=sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for a in arr:
    start, end = a
    