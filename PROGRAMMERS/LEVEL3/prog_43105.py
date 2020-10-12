# PROGRAMMERS LEVEL 3
# 정수 삼각형
# https://programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle):
    h = len(triangle)
    memo = [[0] * h for _ in range(h)]
    memo[0][0] = triangle[0][0]
    answer = 0
    for i in range(h):
        for j in range(i + 1):
            if j == 0:
                memo[i][j] = memo[i - 1][j] + triangle[i][j]
            elif j == i:
                memo[i][j] = memo[i - 1][j - 1] + triangle[i][j]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1]) + triangle[i][j]

            if i == h - 1:
                answer = max(answer, memo[i][j])

    return answer

a = solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
print(a)