# PROGRAMMERS LEVEL 3
# 야근 지수
# https://programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer

    works.sort(key=lambda work: -work)

    i = 0
    while i < len(works):
        if works[0] == works[i]:
            i += 1
            continue
        work = works[0] - works[i]
        if n > work * i:
            n -= work * i
            works[0] = works[i]
        else:
            break

    for j in range(i):
        works[j] = works[0]


    j = 0
    while j < n:
        works[j % i] -= 1
        j += 1

    answer = sum([elem**2 for elem in works])
    return answer

works = [2, 1, 2]
n = 1
result = solution(n, works)
print(result)