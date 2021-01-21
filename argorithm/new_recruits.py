import sys

T = int(input())

for _ in range(T):
    N = int(input())
    input_value = sorted([tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)], key=lambda x: x[0])
    cnt = 1
    interview = input_value[0][1]

    for i in range(1, N):
        if input_value[i][1] < interview:
            cnt += 1
            interview = input_value[i][1]
    print(cnt)
