import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
words = [list(input().rstrip()) for _ in range(N)]
all_words_duplicate = set(sum(words, []))
num = [i for i in range(10)]

# # 순열
# perm = set(permutations(num, len(all_words_duplicate)))

for p in set(permutations(num, len(all_words_duplicate))):
    # print(list(zip(all_words_duplicate, p)))
    # print(p)
    for key, value in list(zip(all_words_duplicate, p)):
        print(key, value)
        for word in words:
            pass
# 숫자 이어 붙힘

# 계산해

# 최댓값
