# BAEK
# RGB 거리 2
# https://www.acmicpc.net/problem/17404

import sys
rl = sys.stdin.readline

n = int(rl())
colors = []

for _ in range(n):
  colors.append(list(map(int, rl().split())))

inf = 1000 * 1000 + 1

# print(colors)

def get_low_cost(k):
  costs = [[0]*3 for _ in range(n)]
  for l in range(3):
    if l == k: 
      costs[0][l] = colors[0][k]
    else:
      costs[0][l] = inf

  for i in range(1, n):
    for j in range(3):
      if i == n-1 and j == k:
        costs[i][j] = inf
      else:
        costs[i][j] = min(costs[i-1][(j+1)%3], costs[i-1][(j+2)%3]) + colors[i][j]
    # print(costs)

  return min(costs[-1])

print(min([get_low_cost(x) for x in range(3)]))
