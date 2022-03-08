# BAEK
# 우수 마을
# https://www.acmicpc.net/problem/1949

import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(rl())
visited = [False] * (n+1)
people = [0, *list(map(int, rl().split()))]
graph = {i: [] for i in range(1, n+1)}
dp = [[0, people[i]] for i in range(n+1)]

def dfs(cur):
  visited[cur] = True

  for nxt in graph[cur]:
    if visited[nxt]: continue
    dfs(nxt)
    dp[cur][1] += dp[nxt][0]
    dp[cur][0] += max(dp[nxt][0], dp[nxt][1])

for _ in range(n-1):
  a, b = map(int, rl().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)

print(max(dp[1][0], dp[1][1]))
