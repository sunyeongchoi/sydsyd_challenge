def removeZero(val):
    removedZeroCnt = 0
    for index, i in enumerate(val):
        if i == '0':
            removedZeroCnt += 1
    return removedZeroCnt, ''.join(val).replace('0', '')

def transform(val):
    namosi = []
    while val != 1:
        rest = val % 2
        val = val // 2
        namosi.append(str(rest))
    namosi.append('1')
    namosi.reverse()
    return namosi

def solution(s):
    answer = []
    zeroCnt = 0
    transCnt = 0
    listedVal = list(s)
    while listedVal:
        # 0 제거
        removedZeroCnt, val = removeZero(listedVal)
        print(removedZeroCnt, val)
        zeroCnt += removedZeroCnt
        # 0 제거 후 길이 확인
        removedStringLen = len(val)
        print(removedStringLen)
        # 이진 변환
        listedVal = transform(removedStringLen)
        transCnt += 1
        if len(listedVal) == 1 and listedVal[0] == "1":
            break
    answer.append(transCnt)
    answer.append(zeroCnt)
    return answer

if __name__ == '__main__':
    result = solution("110010101001")
    print(result)