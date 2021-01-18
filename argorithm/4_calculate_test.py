import sys
from collections import deque

# 입력
s, t = map(int, input().split())
# 큐 생성
queue = deque()
# 중복 불가능 하게 하기 위해 set을 사용(이미 계산된 값이 존재하면 큐에 집어넣지 않도록 체크하기 위해)
check = set()
# 큐에 들어갈 첫 값엔 입력값 s와 부호는 빈값으로 둠
queue.append((s, ''))
# check에 s 넣는다
check.add(s)
# s와 t는 10의 9제곱 이하
MAX = 10e9

if s == t:
    print(0)
else:
    res = -1
    while queue:
        c_v, c_s = queue.popleft()
        if c_v == t:
            res = c_s
            print(res)
            exit(0)

        n_v = c_v * c_v
        if 0 <= n_v <= MAX and n_v not in check:
            queue.append((n_v, c_s+'*'))
            check.add(n_v)

        n_v = c_v + c_v
        if 0 <= n_v <= MAX and n_v not in check:
            queue.append((n_v, c_s+'+'))
            check.add(n_v)

        n_v = 1
        if n_v not in check:
            queue.append((n_v, c_s+'/'))
            check.add(n_v)
    print(res)
