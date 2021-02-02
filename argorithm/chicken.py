import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
location_home, location_chicken, answer2 = [], [], []

for index1, row in enumerate(graph):
    for index2, val in enumerate(row):
        if val == 1: location_home.append((index1, index2))
        elif val == 2: location_chicken.append((index1, index2))

for chicken in combinations(location_chicken, M):
    sum = 0
    for h_x, h_y in location_home:
        answer = []
        for c_x, c_y in chicken:
            answer.append(abs(c_x-h_x) + abs(c_y-h_y))
        sum += min(answer)
    answer2.append(sum)

print(min(answer2))
