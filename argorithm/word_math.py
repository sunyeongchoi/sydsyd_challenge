import sys
input = sys.stdin.readline

N = int(input())
words = [list(input().rstrip()) for _ in range(N)]

word_dict = {}

for word in words:
    k = len(word)-1
    for w in word:
        if w in word_dict:
            word_dict[w] += 10 ** k
        else:
            word_dict[w] = 10 ** k
        k -= 1

sorted_word = sorted(word_dict.values(), reverse=True)
answer, num = 0, 9
for sw in sorted_word:
    answer += sw * num
    num -= 1
print(answer)
