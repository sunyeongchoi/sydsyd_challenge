'''
문제 :
주어진 숫자가 소수 일 경우 1을 return
소수가 아닐 경우 약수 중 1을 제외한 가장 작은 숫자 return

아직 푸는중임!~!!!!
'''

def is_prime(n):
    answer = []
    for i in range(2, n):
        if n % i == 0:
            answer.append(i)
            n = n//i
        else:
            return 1
    return min(answer)


if __name__ == '__main__':
    real_answer = is_prime(24)
    print(real_answer)
