import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer1 = {}
answer2 = {}
for i in range(1, N+1):
    val = input().strip() 
    answer1[i] = val
    answer2[val] = i

for _ in range(M):
    val = input().strip()
    if val.isdigit():
        print(answer1[int(val)])
    else:
        print(answer2[val])
    