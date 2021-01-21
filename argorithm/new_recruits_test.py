import sys

T = int(input())
input_all = []
for _ in range(T):
    N = int(input())
    input_value = sorted([tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)], key=lambda x: x[0])
    input_all.append(input_value)

for test_case in input_all:
    cnt = 1
    interview = test_case[0][1]
    for i in range(1, len(test_case)):
        if test_case[i][1] < interview:
            cnt += 1
            interview = test_case[i][1]
    print(cnt)
