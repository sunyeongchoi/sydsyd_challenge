import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rel = [list(map(int, input().split())) for _ in range(M)]
sort_rel = {}
for i in range(0, N):
    sort_rel[i] = []

global friend
zero = True


def isFriend(k):
    friend.append(k)
    print('friend : ', friend)
    if len(friend) == 5:
        return True
    # for v in dic[k]:
    #     if v not in friend:
    #         return isFriend(v, dic)
    #     else:
    #         pass
    for v in sort_rel[k]:
        if v not in friend:
            ans = isFriend(v)
            friend.remove(v)
            if ans == 1:
                return ans


for x, y in rel:
    sort_rel[x].append(y)
    sort_rel[y].append(x)


for key in sort_rel.keys():
    friend = []
    if isFriend(key):
        print(1)
        zero = False
        break
if zero:
    print(0)
