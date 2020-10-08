# 2018 KAKAO BLIND
# [1차] 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

import re

def is_elem(s):
    p = re.compile('[^a-z]')
    if p.search(s) is None:
        return True
    else:
        return False

def solution(str1, str2):
    answer = 0

    list_str1 = []
    list_str2 = []
    str1, str2 = str1.lower(), str2.lower()

    for i in range(len(str1) - 1):
        if is_elem(str1[i: i+2]):
            list_str1.append(str1[i: i+2])

    for i in range(len(str2) - 1):
        if is_elem(str2[i: i+2]):
            list_str2.append(str2[i: i+2])

    if (len(list_str1) == 0) and (len(list_str2) == 0):
        answer = 1

    else:
        chk_set = set(list_str1) | set(list_str2)
        union_num = 0
        inter_num = 0

        for chk_word in chk_set:
            count1 = list_str1.count(chk_word)
            count2 = list_str2.count(chk_word)
            union_num += max(count1, count2)
            inter_num += min(count1, count2)

        answer = inter_num / union_num

    return int(answer * 65536)

str1 = 'aa1+aa2'
str2 = 'AAAA12'

a = solution(str1, str2)
print(a)
