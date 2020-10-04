def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant,completion):
        if p != c:
            return p
    return participant[-1]


if __name__ == '__main__':
    real_answer = solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'])
    print(real_answer)
