import sys

T = int(sys.stdin.readline())

dq = [0, 1, 2, 4]
for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(len(dq), n+1):
        dq.append(dq[i-1]+dq[i-2]+dq[i-3])
    print(dq[n])