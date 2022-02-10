# BAEK
# 별자리 만들기
# https://www.acmicpc.net/problem/4386

import sys
rl = sys.stdin.readline

import math
import heapq

def get_distance(a, b):
  return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def find(a, parent):
  if a == parent[a]:
    return parent[a]
  
  parent[a] = find(parent[a], parent)
  return parent[a]

def union(a, b, parent):
  a = find(a, parent)
  b = find(b, parent)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a



n = int(rl())
stars = []
edges = []
parent = [i for i in range(n)]

# print(parent)

for _ in range(n):
  x, y = map(float, rl().split())
  stars.append((x, y))

# print(stars)

for i in range(n-1):
  for j in range(i+1, n):
    heapq.heappush(edges, (get_distance(stars[i], stars[j]), i, j))

# print(edges)

distance = 0

while edges:
  d, u, v = heapq.heappop(edges)
  if find(u, parent) == find(v, parent):
    continue

  union(u, v, parent)
  distance += d

print(round(distance, 2))