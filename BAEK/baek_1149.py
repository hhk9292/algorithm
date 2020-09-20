# BAEK
# RGB거리
# https://www.acmicpc.net/problem/1149

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input().rstrip('\n'))
rgb_price = [list(map(int, input().split())) for _ in range(N)]
memo = [[None] * 3 for _ in range(N)]

def get_price(i, j):

    if i == N-1:
        return rgb_price[i][j]

    if memo[i][j] is not None:
        return memo[i][j]

    temp = []
    for k in range(3):
        if j == k:
            continue
        else:
            temp.append(get_price(i+1, k) + rgb_price[i][j])

    memo[i][j] = min(temp)
    return memo[i][j]

min_cost = min(get_price(0, 0), get_price(0, 1), get_price(0, 2))
print(min_cost)