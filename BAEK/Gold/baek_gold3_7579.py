# BAEK
# 앱
# https://www.acmicpc.net/problem/7579
import sys
rl = sys.stdin.readline

n, m = map(int, rl().split())
mems = [0, *list(map(int, rl().split()))]
costs = [0, *list(map(int, rl().split()))]

# print (n ,m, mem, cost)

sum_cost = sum(costs) + 1
dp = [[0 for _ in range(sum_cost)] for _ in range(len(costs))]
result = sum_cost


for i in range(len(costs)):
  if i == 0: continue
  cost = costs[i]
  mem = mems[i]
  for j in range(1, sum_cost):
    if cost > j:
      dp[i][j] = dp[i-1][j]
    
    else:
      dp[i][j] = max(dp[i-1][j-cost] + mem, dp[i-1][j])
    
    if dp[i][j] >= m and result > j:
      result = j

print(result)

# for row in dp:
#   print(row)