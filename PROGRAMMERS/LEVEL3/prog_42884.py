# PROGRAMMERS LEVEL 3
# 단속카메라
# https://programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    answer = 0
    routes.sort(key=lambda route: route[1])
    camera = -30001
    for route in routes:
        if route[0] > camera:
            answer += 1
            camera = route[1]
    return answer


routes= [[-20, -15], [-14,-5], [-18,-13], [-5,-3]]
a = solution(routes)
print(a)