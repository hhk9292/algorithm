# PROGRAMMERS LEVEL 3
# 2 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):

    tile = [0] * 60001
    tile[1] = 1
    tile[2] = 2

    i = 3
    while i <= n:
        tile[i] = tile[i - 2] + tile[i - 1]
        tile[i] %= 1000000007
        i += 1

    answer = tile[n]
    return answer

n = 4
a = solution(n)
print(a)