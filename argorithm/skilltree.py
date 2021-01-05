def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)

        for s in skill_tree:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer


if __name__ == '__main__':
    real_answer = solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA'])
    print('정답 : ', real_answer)
