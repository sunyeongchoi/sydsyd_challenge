import math

# 적절한 명령어가 들어갔는지 테스트하는 함수
def program_commandCheck(program, flag_rules, command):
    # flag_rule_manufactor 함수에 flag_rules를 넣어 보기 좋게 나온 dict 값을 꺼낸다.
    flag_rule_dict = flag_rule_manufactor(flag_rules)
    print('flag_rule_dict : ', flag_rule_dict)
    # 하나의 명령에 대해서 공백을 기준으로 list에 넣는다.
    command_list = command.split()
    # 가장 앞에 값은 program이랑 비교를 해야하기 때문에 pop으로 꺼내서 비교
    # program값과 다르다면 False 리턴
    if command_list.pop(0)!=program:
        return False
    # flag와 flag_argument_type을 확인하여 알맞은 값이 들어갔는지 확인
    # NULL인 경우를 제외하고는 2개씩 짝을 이루기 때문에 4개의 값이 들어있으면 2번, 5개의 값이 들어있으면 3번 반복문을 돌린다.
    # python의 경우 0.5를 반올림 하면 0이 나오기 때문에 0.1을 더한 뒤 반올림 해주었다.
    for _ in range(round(len(command_list)/2+0.1)):
        comm = command_list.pop(0)
        # 만약 처음으로 꺼낸 값에 - 가 들어있지 않다면 올바른 형식이 아니므로 False리턴
        if not comm.count('-'):
            return False
        # flag_rule_dict에서 key값을 comm으로 두고 하나하나 확인한다.
        comm_type = flag_rule_dict[comm]
        # STRING인데 문자가 아닐 경우 False
        if comm_type == 'STRING':
            if command_list:
                if not(command_list.pop(0).isalpha()):
                    return False
            else:
                return False

        # STRINGS인데 문자가 아닐 경우 False
        if comm_type == 'STRINGS':
            if command_list:
                while command_list[0].count('-')==0:
                    if not(command_list.pop(0).isalpha()):
                        return False
            else:
                return False
        
        # NUMBER인데 숫자가 아닐 경우 False
        elif comm_type == 'NUMBER':
            if command_list:
                if not(command_list.pop(0).isdigit()):
                    return False
            else:
                return False
        
        # NUMBERS인데 숫자가 아닐 경우 False
        elif comm_type == 'NUMBERS':
            if command_list:
                while command_list[0].count('-')==0:
                    if not(command_list.pop(0).isdigit()):
                        return False
            else:
                return False

        # NULL이고 다음에 문자가 남아있을경우, 그 문자가 -를 포함하고 있지 않으면 argument가 들어갔단 소리니 False
        elif comm_type == 'NULL':
            if command_list:
                if command_list[0].count('-')>0:
                    return False
    # 이외에는 True 리턴
    return True

# flag_rules를 보기 좋게 dict에 넣는 함수
# -n ALIAS -num
def flag_rule_manufactor(flag_rules):
    flag_rule_dict = dict()
    
    for fr in flag_rules:
        temp = []
        val = fr.split()
        print('val : ', val)
        if 'ALIAS' in val:
            temp.append(val[0])
            temp.append(val[2])
        else:
            flag_name, flag_argument_type = val
            flag_rule_dict[flag_name]=flag_argument_type
        print('temp : ', temp)
        if temp:
            for t in temp:
                print('flag_rule_dict : ', flag_rule_dict)
                print('flag_rule_dict.keys() : ', flag_rule_dict.keys())
                if t in flag_rule_dict.keys():
                    value = flag_rule_dict[t]
                
            for t in temp:
                flag_rule_dict[t]=value
    return flag_rule_dict

# 메인 함수
def solution(program, flag_rules, commands):
    answer = []
    # 한 개의 명령 씩 꺼내서 나온 결과를 answer 에 append
    for command in commands:
        result = program_commandCheck(program, flag_rules, command)
        answer.append(result)
    return answer

if __name__ == '__main__':
    print(solution("bank", ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"], ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))