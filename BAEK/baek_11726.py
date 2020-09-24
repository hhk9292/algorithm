# BAEK
# 2*n 타일링
# https://www.acmicpc.net/problem/11726

import sys
input = sys.stdin.readline

N = int(input().rstrip())

tiles = [0] * max((N + 1), 3)
tiles[1] = 1
tiles[2] = 2

if N >= 3:
    for i in range(3, N+1):
        tiles[i] = tiles[i - 1] + tiles[i - 2]
print(tiles[N] % 10007)
