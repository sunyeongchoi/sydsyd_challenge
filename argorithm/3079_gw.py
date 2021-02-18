import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
def sol(m):
    i = 1           # 불가능한 시간의 최댓값
    M = m*arr[0]    # 가능한 시간의 최댓값
    if len(arr)== 1:
        return M
    while M-i>=2:
        j = (i+M)//2 # 중간값
        s = 0        # 심사 받은 인원의 수
        for a in arr:   
            if s < m:     # 현재 m명 미만 검사했으면 계속 검사 
                s += j//a
            else:         # 현재 m명 이상 검사 가능하면 그만
                break
        if s >= m:  # m명보다 더 검사했으면 시간의 최댓값 M을 중간값 j로 교체      
            M = j
        else:       # m명보다 더 적게 검사했으면 시간의 최솟값 i를 중간값 j로 교체
            i = j
    return M
print(sol(m))