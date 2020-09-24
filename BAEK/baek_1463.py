# BAEK
# 1로 만들기
# https://www.acmicpc.net/problem/1463

import sys
input = sys.stdin.readline

N = int(input().rstrip())
cals = [float('inf')] * (N+1)
cals[1] = 0
for i in range(1, N+1):
    if i + 1 <= N:  # +1
        cals[i + 1] = min(cals[i] + 1, cals[i + 1])
    if i * 2 <= N:  # *2
        cals[i * 2] = min(cals[i] + 1, cals[i * 2])
    if i * 3 <= N:  # *3
        cals[i * 3] = min(cals[i] + 1, cals[i * 3])

print(cals[N])

