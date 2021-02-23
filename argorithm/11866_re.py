from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
q = deque([])
for i in range(1, N+1):
    q.append(i)

print('<', end='')
while q:
    for i in range(K-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end='')
    if q:
        print(',', end=' ')
print('>', end='')