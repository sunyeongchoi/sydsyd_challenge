import sys
input = sys.stdin.readline

N = int(input())

result = [0 for _ in range(N+1)]
result[1]=0
for i in range(2, N+1):
    result[i] = result[i-1]+1
    if i%2==0:
        result[i] = min(result[i//2]+1, result[i])
    if i%3==0:
        result[i] = min(result[i//3]+1, result[i])

print(result[N])