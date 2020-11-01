# PROGRAMMERS LEVEL 2
# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for char in s:
        try:
            top = stack[-1]
            if char == top:
                del stack[-1]
            else:
                stack.append(char)
        except IndexError:
            stack.append(char)
    if len(stack):
        answer = 0
    else:
        answer = 1
    return answer


# test case
# result = 1

s = 'baabaa'
result = solution(s)
print(result)