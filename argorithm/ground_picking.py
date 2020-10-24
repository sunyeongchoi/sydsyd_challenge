def solution(land):
    n = len(land)-1
    for i in range(n):
        print('land[i][1], land[i][2], land[i][3]', land[i][1], land[i][2], land[i][3])
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        print('land[',i,'+1][0]', land[i+1][0])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[n][0], land[n][1], land[n][2], land[n][3])


if __name__ == '__main__':
    real_answer = solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
    print(real_answer)

