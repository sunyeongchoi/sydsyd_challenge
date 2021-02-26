def solution(s1, s2):
    answer = set()
    min_val = min(len(s1), len(s2))
    for i in range(min_val):
        if s1[-i:] == s2[:i]:
            answer.add(s1+s2[i:])
        
        if s2[-i:] == s1[:i]:
            answer.add(s2+s1[i:])
    return min(sorted(answer), key=lambda x: len(x))

if __name__ == '__main__':
    real_answer = solution('AxA', 'AyA')
    print(real_answer)