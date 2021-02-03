import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan_length = [int(input()) for _ in range(K)]

start = 1
end = max(lan_length)
answer = []
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for length in lan_length:
        cnt += length//mid
    if cnt >= N:
        start = mid+1
        answer.append(mid)
    else:
        end = mid-1
print(max(answer))
