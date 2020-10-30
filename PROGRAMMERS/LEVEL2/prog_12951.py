# PROGRAMMERS LEVEL 2
# JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def is_char(s):
    if 'a' <= s <= 'z':
        return True
    return False

def solution(s):
    answer = ''
    s = list(s.lower())
    for i in range(len(s)):
        if ((i == 0) and is_char(s[i])) or ((s[i - 1] == ' ') and is_char(s[i])):
            s[i] = s[i].upper()
    return ''.join(s)

