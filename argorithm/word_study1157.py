from collections import defaultdict

word = list(input().lower())

cnt_dict = defaultdict(int)
for w in word:
    cnt_dict[w] += 1

answer = max(cnt_dict.keys(),key=lambda x: cnt_dict[x])
print(answer.upper())
