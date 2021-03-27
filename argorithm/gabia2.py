def solution(s):
    answer = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            word = s[i:j]
            if len(word) == (len(set(word))):
                answer.add(word)
    return len(answer)

if __name__ == '__main__':
    print(solution('abac'))