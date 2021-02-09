import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    answer = ''
    R, S = map(str, input().split())
    word = list(S)
    for w in word:
        answer += str(w)*int(R)
    print(answer)