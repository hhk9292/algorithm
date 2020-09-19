# BAEK
# 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
sum_table = [[0] * N for _ in range(N)]

for i in range(N):
    acc = 0
    for j in range(N):
        if i == 0:
            if j == 0:
                sum_table[i][j] = table[i][j]
            else:
                sum_table[i][j] = sum_table[i][j-1] + table[i][j]
        else:
            acc += table[i][j]
            sum_table[i][j] = sum_table[i-1][j] + acc

def int_minus_one(num):
    return int(num) - 1

for _ in range(M):
    x1, y1, x2, y2 = map(int_minus_one, input().split())

    if x1 > 0:
        if y1 > 0:
            result = sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1]
        else:
            result = sum_table[x2][y2] - sum_table[x1-1][y2]

    else:
        if y1 > 0:
            result = sum_table[x2][y2] - sum_table[x2][y1-1]
        else:
            result = sum_table[x2][y2]

    print(result)
