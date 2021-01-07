import datetime


def solution(a, b):
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    yoil_index = datetime.datetime(2016, a, b).weekday()
    return weekday[yoil_index]


if __name__ == '__main__':
    real_answer = solution(5, 24)
    print('정답 : ', real_answer)
