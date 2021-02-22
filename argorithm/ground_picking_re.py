def solution(land):
    index = len(land)-1
    for i in range(index):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[index][0], land[index][1], land[index][2], land[index][3])



if __name__ == '__main__':
    real_answer = solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
    print(real_answer)

