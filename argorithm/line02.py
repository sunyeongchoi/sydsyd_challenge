import re 
from itertools  import groupby

def solution(inp_str):
    flag = True
    answer = []
    # 1번 조건
    if not (8<=len(inp_str)<=15):
        flag = False
        answer.append(1)
    # 2번 조건
    if not (inp_str == ''.join(re.findall('[a-zA-Z0-9가-힣~!@#$%^&*]', inp_str))):
        flag = False
        answer.append(2)
    # 3번 조건
    valid=0
    if re.search('[0-9]', inp_str) is not None: valid += 1
    if re.search('[a-z]', inp_str) is not None: valid += 1
    if re.search('[A-Z]', inp_str) is not None: valid += 1
    if re.search('[~!@#$%^&*]', inp_str) is not None: valid += 1
    if valid < 3:
        flag = False
        answer.append(3)
    # 4번 조건
    if max([len(list(g)) for k,g in groupby(inp_str)], default=0) >= 4:
        answer.append(4)
    # 5번 조건
    for inp in inp_str:
        if inp_str.count(inp) >= 5:
            flag = False
            answer.append(5)
    
    if flag:
        answer.append(0)

    return sorted(set(answer))