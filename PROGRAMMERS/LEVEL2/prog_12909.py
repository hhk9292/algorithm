# PROGRAMMERS LEVEL 2
# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for letter in s:
        if letter == '(':
            stack.append(letter)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

    if len(stack) > 0:
        return False
    return True



s = '(()('
answer = solution(s)
print(answer)