import sys
from itertools import combinations
input = sys.stdin.readline

answer = []
in_value = [int(input()) for _ in range(9)]

# combinations를 사용하여 in_value에 존재하는 값 중에서 7개의 값을 뽑은 경우를 구한다
# permutations과 다르게 combinations는 순서는 상관하지 않는다.(조합)
all_cases = combinations(in_value, 7)

# 합이 100인 경우가 답이다.
for case in all_cases:
    if sum(case) == 100:
        answer = case
        break

# 값을 한 개씩 출력하기 위해 for문 사용
for i in answer:
    print(i)
