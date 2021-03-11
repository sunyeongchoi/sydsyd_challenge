import sys; input=sys.stdin.readline
from itertools import combinations

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
comb_arr = list(combinations(sorted(arr), 3))
answer = []
for co in comb_arr:
    min = 10**9+1
    for i in range(c-1):
        if min > abs(co[i]-co[i+1]):
            min = abs(co[i]-co[i+1])
    answer.append(min)
print(max(answer))
        
