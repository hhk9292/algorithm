# BAEK
# 운동
# https://www.acmicpc.net/problem/1956

import sys
rl = sys.stdin.readline

inf = 400 * 10000 + 1
v, e = map(int, rl().split())

dist = [[inf] * (v+1) for _ in range(v+1)]

for _ in range(e):
  a, b, w = map(int, rl().split())
  if w < dist[a][b]:
    dist[a][b] = w

for i in range(1, v+1):
  for j in range(1, v+1):
    for k in range(1, v+1):
      if i == k or k == j: continue
      if dist[i][k] + dist[k][j] < dist[i][j]:
        dist[i][j] = dist[i][k] + dist[k][j]

# for row in dist:
#   print(row)

min_dist = inf

for i in range(1, v+1):
  if dist[i][i] < min_dist:
    min_dist = dist[i][i]

if min_dist == inf:
  print(-1)
else:
  print(min_dist)