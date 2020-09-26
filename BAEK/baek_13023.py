# BAEK
# 램프
# https://www.acmicpc.net/problem/13023
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
friends = {}
for i in range(N):
    friends[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visit = [True] * N
def dfs(i, depth):
    global ans
    if ans:
        return
    if depth == 4:
        ans = True
        return True

    for friend in friends[i]:
        if visit[friend]:
            visit[friend] = False
            dfs(friend, depth + 1)
            visit[friend] = True
    return False

ans = False
for i in range(N):
    visit[i] = False
    dfs(i, 0)
    visit[i] = True

if ans:
    print(1)
else:
    print(0)