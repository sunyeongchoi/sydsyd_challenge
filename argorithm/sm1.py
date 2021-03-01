import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    skill = input().split()
    k = int(input())
    relation = list(input().split() for _ in range(k))

    temp = defaultdict(list)
    for r in relation:
        temp[r[0]] += r[1]

    # while skill:
    #     s = skill.pop(0)
    #     if s in temp:
    #         for val in temp.values():
    #             if val in temp:
                    
    #             else:
    #                 print(s, val)
    

    for t in temp:
        for tval in temp[t]:
            print(t, tval)
            if tval in temp:
                for val in temp[tval]:
                    print()



if __name__=="__main__":
    main()