from collections import defaultdict

word = list(input().lower())

cnt_dict = defaultdict(int)
for w in word:
    cnt_dict[w] += 1

max_num = max(cnt_dict.values())
if list(cnt_dict.values()).count(max_num) > 1:
    print('?')
else:
    print(max(cnt_dict.keys(),key=lambda x: cnt_dict[x]).upper())
