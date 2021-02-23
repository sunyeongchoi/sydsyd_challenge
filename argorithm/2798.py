from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

comb_list = list(combinations(arr, 3))

max = -1
for c in comb_list:
    if sum(c) <= M and sum(c) > max:
        max = sum(c)

print(max)

