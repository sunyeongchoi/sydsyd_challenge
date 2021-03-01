import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    skill = input().split()
    k = int(input())
    relation = list(input().split() for _ in range(k))

    min_val = min(len(s1), len(s2))
    for i in range(min_val):
        if s1[-i:] == s2[:i]:
            answer.add(s1+s2[i:])
        
        if s2[-i:] == s1[:i]:
            answer.add(s2+s1[i:])
    return min(sorted(answer), key=lambda x: len(x))
    



if __name__=="__main__":
    main()

