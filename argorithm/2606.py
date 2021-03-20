import sys; input=sys.stdin.readline
from collections import defaultdict

# 함수 구현
def dfs(arr, visited, num):
    global answer
    visited[num] = 1
    for a in arr[num]:
        if not visited[a]:
            answer += 1
            dfs(arr, visited, a)

# 변수 설정
computer_cnt = int(input())
linked_cnt = int(input())
arr_dict = defaultdict(list)
for a in [list(map(int, input().split())) for _ in range(linked_cnt)]:
    arr_dict[a[0]].append(a[1])
    arr_dict[a[1]].append(a[0])
visited = [0]*(computer_cnt+1)
answer = 0

# dfs 실행
dfs(arr_dict, visited, 1)
print(answer)