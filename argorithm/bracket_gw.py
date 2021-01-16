import sys
input = sys.stdin.readline
T = int(input())


def sol(p):
    stack = []
    for k in p:
        if k == '(':
            stack.append(k)
            print(stack)
        else:
            if not stack:
                return 'NO'
            t = stack.pop()
            print(t)
    if stack:
        return 'NO'
    return 'YES'


for _ in range(T):
    p = input().strip()
    print(sol(p))
