# PROGRAMMERS LEVEL 2
# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

import math

def solution(brown, yellow):
    yellow += brown
    brown += 4

    w = (brown + math.sqrt(brown ** 2 - 16 * yellow)) // 4
    h = (brown - math.sqrt(brown ** 2 - 16 * yellow)) // 4
    w, h = int(w), int(h)

    answer = [w, h]
    return answer

brown = 10
yellow = 2
answer = solution(brown, yellow)
print(answer)