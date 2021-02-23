from collections import deque
import sys
input = sys.stdin.readline
q = deque()

N = int(input())
for _ in range(N):
    val = input().rstrip()
    if ' ' in val:
        comm, num = val.split()
        if comm == 'push':
            q.append(num)
    elif val == 'pop':
        if len(q)==0: print(-1)
        else: print(q.pop())
    elif val == 'size':
        print(len(q))
    elif val == 'empty':
        if len(q)==0: print(1)
        else: print(0)
    else:
        if len(q)==0: print(-1)
        else: print(q[-1])