from collections import deque
import sys
input = sys.stdin.readline
q = deque()

N = int(input())
for _ in range(N):
    val = input().rstrip()
    if ' ' in val:
        command, num = val.split()
        if command == 'push': 
            q.append(num)
    else:
        if val == 'front': 
            if len(q) == 0: print(-1)
            else: print(q[0])
        elif val == 'back': 
            if len(q)==0: print(-1)
            else: print(q[-1])
        elif val == 'size': print(len(q))
        elif val == 'empty':
            print(1 if len(q)==0 else 0)
        elif val == 'pop':
            if len(q)==0: print(-1)
            else: print(q.popleft())
        




