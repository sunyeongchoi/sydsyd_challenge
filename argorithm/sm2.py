import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    p, n, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(1, p+1):
        sumval = 0
        for a in arr:
            if a[0]==i and a[1]<=h:
                sumval+=1000*a[1]
        print(i, sumval)


if __name__=="__main__":
    main()