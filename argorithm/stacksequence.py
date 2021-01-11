import sys

input = sys.stdin.readline
n = int(input())
given = [int(input()) for _ in range(n)] # 주어진 수열


def solution():
    cnt, stack, result = 1, [], []
    for i in given:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)


print(solution())
