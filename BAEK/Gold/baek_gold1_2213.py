# BAEK
# 트리의 독립집합
# https://www.acmicpc.net/problem/2213

import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(rl())
nodes = [0, *list(map(int, rl().split()))]
graph = {i: [] for i in range(1, n+1)}
dp = [[0, nodes[i]] for i in range(n+1)]
trees = [[[], [i]] for i in range(n+1)]
visit = [False] * (n+1)
visit[0] = True

for _ in range(n-1):
  a, b = map(int, rl().split())
  graph[a].append(b)
  graph[b].append(a)

# print(nodes)
# print(graph)
# print(dp)
# print(trees)

def dfs(cur):
  visit[cur] = True
  
  for nxt in graph[cur]:
    if visit[nxt]: 
      continue
    dfs(nxt)

    # 현재 노드를 뽑는경우 => 다음 노드를 뽑으면 안됨
    dp[cur][1] += dp[nxt][0]
    for i in trees[nxt][0]:
      trees[cur][1].append(i)

    # 현재 노드를 안뽑는 경우
    if dp[nxt][1] > dp[nxt][0]:
      dp[cur][0] += dp[nxt][1]
      for i in trees[nxt][1]:
        trees[cur][0].append(i)
    
    else:
      dp[cur][0] += dp[nxt][0]
      for i in trees[nxt][0]:
        trees[cur][0].append(i)

dfs(1)
# print(dp)
# print(trees)

if dp[1][0] > dp[1][1]:
  max_w = dp[1][0]
  max_t = trees[1][0]

else:
  max_w = dp[1][1]
  max_t = trees[1][1]

max_t.sort()
print(max_w)
print(*max_t)