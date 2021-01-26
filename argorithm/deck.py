import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()

for i in range(N):
    value = input().rstrip()
    if " " in value:
        name, num = value.split()
        if name == 'push_back':
            dq.append(num)
        elif name == 'push_front':
            dq.appendleft(num)
    elif value == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            pop = dq.popleft()
            print(pop)
    elif value == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            pop = dq.pop()
            print(pop)
    elif value == 'size':
        print(len(dq))
    elif value == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif value == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif value == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq)-1])
