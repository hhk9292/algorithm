# BAEK
# 줄 세우기
# https://www.acmicpc.net/problem/2252

import sys
rl = sys.stdin.readline

from collections import deque

n, m = map(int, rl().split())

# taller[a]: a 보다 큰 사람들
tallers = [[] for _ in range(n+1)]

# num_of_smaller[a]: a 보다 작은 사람들 숫자
num_of_smallers = [0] * (n+1)
num_of_smallers[0] = None

for _ in range(m):
  # a가 b보다 작음 => a 가 앞에 서야함
  a, b = map(int, rl().split())
  num_of_smallers[b] += 1
  tallers[a].append(b)

# print(smaller)
# print(num_of_smaller)

q = deque()

for (i, no) in enumerate(num_of_smallers):
  if no == 0:
    q.append(i)

line = []

while q:
  cur = q.popleft()
  line.append(cur)

  for taller in tallers[cur]:
    num_of_smallers[taller] -= 1
    if num_of_smallers[taller] == 0:
      q.append(taller)

print(*line)