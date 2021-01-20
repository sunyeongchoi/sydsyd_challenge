from collections import deque

F, S, G, U, D = map(int, input().split())

stack = deque([(S, 0)])
visited = {S}
while stack:
    floor, cnt = stack.popleft()
    if floor == G:
        print(cnt)
        exit(0)
    if floor + U <= F and floor + U not in visited:
        stack.append((floor+U, cnt+1))
        visited.add(floor+U)
    if floor - D >= 1 and floor - D not in visited:
        stack.append((floor-D, cnt+1))
        visited.add(floor-D)
print('use the stairs')