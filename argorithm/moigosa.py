def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0]*3

    for i, ans in enumerate(answers):
        if ans == first[i % len(first)]:
            cnt[0] += 1
        if ans == second[i % len(second)]:
            cnt[1] += 1
        if ans == third[i % len(third)]:
            cnt[2] += 1

    for index, c in enumerate(cnt):
        if max(cnt) == c:
            answer.append(index+1)

    return answer


if __name__ == '__main__':
    real_answer = solution([1, 3, 2, 4, 2])
    print('정답 : ', real_answer)
