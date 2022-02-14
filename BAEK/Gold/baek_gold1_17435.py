# BAEK
# 합성함수와 쿼리
# https://www.acmicpc.net/problem/17435

import sys
rl = sys.stdin.readline

m = int(rl())
f = [0, *list(map(int, rl().split()))]
MAX = 19 # 500000 < 2**19

fn = [[0] * (m + 1) for _ in range(MAX)]

for j in range(m+1):
  fn[0][j] = f[j]

# print(fn)

for i in range(1, MAX):
  for j in range(1, m+1):
    fn[i][j] = fn[i-1][fn[i-1][j]]

# for row in fn:
#   print(row)

answer = []
q = int(rl())

for _ in range(q):
  n, x = map(int, rl().split())

  for i in range(MAX):
    if n & (1<<i):
      x = fn[i][x]
  
  print(x)

