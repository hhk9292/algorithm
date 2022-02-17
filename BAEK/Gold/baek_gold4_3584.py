# BAEK
# 가장 가까운 공통 조상
# https://www.acmicpc.net/problem/3584

import sys
rl = sys.stdin.readline

def solution():
  n = int(rl())
  parent = [None] * (n+1)

  for _ in range(n-1):
    a, b = map(int, rl().split())
    parent[b] = a
  
  target_a, target_b = map(int, rl().split())
  check = set()
  check.add(target_a)
  while 1:
    if parent[target_a] is None:
      break
    check.add(parent[target_a])
    target_a = parent[target_a]
  
  # print(check)
  while 1:
    if target_b in check:
      break
    target_b = parent[target_b]
  
  # print('check', check)
  # print('answer', target_b)
  print(target_b)
  


t = int(rl())
for _ in range(t):
  solution()