import sys

n = int(sys.stdin.readline())
result = []
r = ''
for i in range(n):
    stack = list(sys.stdin.readline().rstrip())
    sum = 0
    for target in stack:
        if target == '(':
            sum += 1
        elif target == ')':
            sum -= 1
        if sum < 0:
            answer = 'NO'
            break
    if sum == 0:
        answer = 'YES'
    else:
        answer = 'NO'
    result.append(answer)

print('\n'.join(result))
