import math

def solution(grade):
    answer = []
    calc = 0
    # 5로 나눌 경우
    moc = grade//5
    namogi = grade%5
    if namogi!=0:
        # 3으로 나누어 떨어지는지 확인
        if namogi%3==0:
            return namogi//3 + moc
        else:
            
    # 3로 나눌 경우
    grade//3


    # 마지막에는 나머지가 0이여야됨
    # 0이 아닐 경우 -1 출력
    return answer

if __name__ == '__main__':
    real_answer = solution(15)
    print(real_answer)