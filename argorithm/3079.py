import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = [int(input().rstrip()) for _ in range(N)]

result = 0
left = 0
right = M*(min(time))

while left <= right:
    mid = (left+right)//2

    judgePeople = 0
    for t in time:
        judgePeople += mid//t
    
    if judgePeople < M:
        left = mid+1
    else:
        result = mid
        right = mid-1
print(result)