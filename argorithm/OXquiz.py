import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ox = list(input().rstrip())
    cnt = 1
    sum = 0
    for index, i in enumerate(ox):
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
