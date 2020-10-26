# PROGRAMMERS LEVEL 2
# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

import re
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        order = re.sub(f'[^{skill}]', '', skill_tree)
        if order == skill[:len(order)]:
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
a = solution(skill, skill_trees)
print(a)