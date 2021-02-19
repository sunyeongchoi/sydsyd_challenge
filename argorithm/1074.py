import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

def z(x, y, z):
    # 사분면 찾음
    midx, midy = (2**z)//2 + x, (2**z)//2 + y

    if r < midx and c < midy:
        z(midx, midy, z//2)
    elif r < midx and c >= midy:
        num += midx*midy
        z(midx, midy, z//2)
    elif r >= midx and c < midy:
        num += (midx*midy) * 2
        z(midx, midy, z//2)
    else:
        num += (midx*midy) * 3  
        z(midx, midy, z//2)

z(0, 0, N)
print(num)