import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
location_home, location_chicken = [], []

for index1, row in enumerate(graph):
    for index2, val in enumerate(row):
        if val == 1: location_home.append((index1, index2))
        elif val == 2: location_chicken.append((index1, index2))

minv = float('inf')
for chicken in combinations(location_chicken, M):
    sum = 0
    for home in location_home:
        sum += min([abs(chi[0]-home[0]) + abs(chi[1]-home[1]) for chi in chicken])
    if minv > sum:
        minv = sum

print(minv)
