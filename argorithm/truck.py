def solution(bridge_length, weight, truck_weights):
    answer = 0
    present = [0] * bridge_length
    current_weight = 0

    while truck_weights:
        answer += 1
        bridge_out_weight = present.pop(0)
        current_weight -= bridge_out_weight

        if weight < current_weight + present[0]:
            present.append(0)

        else:
            next_truck = truck_weights.pop(0)
            present.append(next_truck)
            current_weight += next_truck

    while current_weight > 0:
        answer += 1
        bridge_out_weight = present.pop(0)
        current_weight -= bridge_out_weight

    return answer


if __name__ == '__main__':
    real_answer = solution(2, 10, [7, 4, 5, 6])
    print(real_answer)
