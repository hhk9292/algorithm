# BAEK
# 이동하기
# https://www.acmicpc.net/problem/11048

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [[0] for _ in range(N+1)]
maze[0].extend([0] * M)
for i in range(N):
    maze[i+1].extend(list(map(int, input().split())))

def local_max(i, j):
    return max(maze[i-1][j], maze[i-1][j-1], maze[i][j-1])

for i in range(1, N+1):
    for j in range(1, M+1):
        maze[i][j] += local_max(i, j)
print(maze[N][M])