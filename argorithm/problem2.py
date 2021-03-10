# 2번
from collections import defaultdict

def remove_duplicate(arr):
    dict = defaultdict(int)
    for a in arr:
        dict[a] += 1
    return dict

if __name__ == '__main__':
    print(remove_duplicate([3,3,3,3,1,1,2,3,6]))