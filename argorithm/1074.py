import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

arr = [[-1]*(2**N) for _ in range(2**N)]
print(arr)
num = 0

def z(start):
    # 사분면 찾음
    midx, midy = (2**N)//2, (2**N)//2
    print(midx, midy)
    # 현재 위치 이전의 사분면에 있는 갯수 다 더함

    # 다시 사분면 찾음    

print(arr[r][c])