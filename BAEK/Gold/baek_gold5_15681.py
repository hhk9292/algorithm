# BAEK
# 트리와 쿼리
# https://www.acmicpc.net/problem/15681

import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10**6)

# from collections import deque

'''
class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.number = 1
  
  def push_child(self, node):
    self.children.append(node)


n, r, q = map(int, rl().split())

tree = [None] * (n+1)
graph = {}

# set graph
for _ in range(n-1):
  u, v = map(int, rl().split())

  if graph.get(u) is None:
    graph[u] = []

  if graph.get(v) is None:
    graph[v] = []
  
  graph[u].append(v)
  graph[v].append(u)

# print(graph)

# set tree
queue = deque()
queue.append(r)
check = set()
check.add(r)

while queue:
  cur = queue.popleft()

  if tree[cur] is None:
    tree[cur] = Node(cur)
    
  node = tree[cur]

  for nxt in graph[cur]:
    if nxt not in check:
      queue.append(nxt)
      check.add(nxt)

      if tree[nxt] is None:
        tree[nxt] = Node(nxt)
      
      child = tree[nxt]
      node.push_child(child)

def count_sub_tree(node):

  if len(node.children) == 0:
    return node.number  # 1
  
  number = 0
  for child in node.children:
    number += count_sub_tree(child)
  
  node.number += number
  return node.number

count_sub_tree(tree[r])


for _ in range(q):
  target = int(rl())
  print(tree[target].number)

'''

n, r, q = map(int, rl().split())

graph = {}

# set graph
for _ in range(n-1):
  u, v = map(int, rl().split())

  if graph.get(u) is None:
    graph[u] = []

  if graph.get(v) is None:
    graph[v] = []
  
  graph[u].append(v)
  graph[v].append(u)

numbers = [1] * (n+1)

def set_numbers():
  check = set()
  def get_numbers(node):
    check.add(node)
    number = 0
    for child in graph[node]:
      if child in check: continue
      number += get_numbers(child)
    
    numbers[node] += number
    return numbers[node]
  
  numbers[r] = get_numbers(r)

set_numbers()

for _ in range(q):
  target = int(rl())
  print(numbers[target])
