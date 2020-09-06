# 2020 KAKAO BLIND
# 2. 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

def is_right(p):
    """ 올바른 괄호 문자열인지 확인


    :param p:
    '(', ')'로 이루어진 문자열


    :return:
    올바른 괄호 문자열이면 True, 아니면 False
    """
    result = False
    opens = []  # 열린 괄호가 들어가는 리스트
    for bracket in p:
        if bracket == "(":
            opens.append("(")
        else:  #  닫힌 괄호면 opens 리스트를 검사
            # 닫힌 괄호가 나왔을 때 opens가 비어있으면 종료 후 False 반환
            if len(opens) == 0:
                break
            else:
                opens.pop()
    # 모든 검사를 마쳤을 때 opens가 비어있으면 True 반환
    else:
        if len(opens) == 0:
            result = True

    # 그렇지 않으면 False 반환
    return result

def reverse_brackets(p):
    """ 괄호를 뒤집어서 반환하는 함수


    :param p:
    '(', ')'로 이루어진 문자열


    :return:
    각 괄호가 뒤집어진 문자열 반환
    ex) reverse_brackets('(())') = '))(('
    """
    result = ''
    for bracket in p:
        if bracket == "(":
            result += ")"
        else:
            result += "("
    return result

def solution(p):
    # 입력이 빈 문자열이거나 올바른 문자열일 경우 그대로 반환
    if (p == '') or (is_right(p)):
        return p
    else:
        open_cnt = 0   # "("의 개수
        close_cnt = 0  # "("의 개수
        for i in range(len(p)):
            if p[i] == "(":
                open_cnt += 1
            else:
                close_cnt += 1
            # 최초의 균형잡힌 괄호 문자열을 찾아서 u에 저장하고 뒷부분 v에 저장
            if open_cnt == close_cnt:
                u = p[: i+1]
                v = p[i+1:]
                break
        
        # u가 올바른 문자열일 경우
        if is_right(u):
            return u + solution(v)
        # 그렇지 않은 경우
        else:
            return "(" + solution(v) + ")" + reverse_brackets(u[1:-1])


