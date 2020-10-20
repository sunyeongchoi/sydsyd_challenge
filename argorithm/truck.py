def solution(bridge_length, weight, truck_weights):
    answer = 0
    present = [0] * bridge_length
    while truck_weights:
        present.append(truck_weights.pop(0))



    return val


if __name__ == '__main__':
    real_answer = solution(2, 10, [7, 4, 5, 6])
    print(real_answer)
