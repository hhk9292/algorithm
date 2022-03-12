# BAEK
# 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049

import sys
rl = sys.stdin.readline

inf = 2**31 - 1

n = int(rl())
dp = [[inf] * (n) for _ in range(n)]
rows = [0] * (n)
cols = [0] * (n)


for i in range(n):
  r, c = map(int, rl().split())
  rows[i] = r
  cols[i] = c

for i in range(n):
  dp[i][i] = 0

for size in range(1, n):
  for s in range(n-size):
    e = s + size

    for m in range(s, e):
      dp[s][e] = min(dp[s][e], dp[s][m] + dp[m+1][e] + rows[s] * cols[m] * cols[e])

# for row in dp:
#   print(row)

print(dp[0][n-1])