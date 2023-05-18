def solution(s):
    zeroCnt = 0
    transCnt = 0
    while True:
        if s == '1':
            break
        # 0 제거
        removedZero = s.count('1')
        zeroCnt += len(s) - removedZero
        # 이진 변환
        s = bin(removedZero)[2:]
        transCnt += 1
    return [transCnt, zeroCnt]

if __name__ == '__main__':
    result = solution("110010101001")
    print(result)