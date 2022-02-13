# BAEK
# 개미굴
# https://www.acmicpc.net/problem/14725

import sys
rl = sys.stdin.readline


class Room:
  def __init__(self, data=None):
    self.data = data
    self.children = {}

class Hive:
  def __init__(self):
    root = Room()
    self.root = root
  
  def push(self, arr):
    parent = self.root
    for i in range(len(arr)):
      v = arr[i]

      if parent.children.get(v) is None:
        child = Room(v)
        parent.children[v] = child
      
      parent = parent.children[v]
  
  def print(self):
    arr = list(self.root.children.keys())
    arr.sort()
    for v in arr:
      self.__print(self.root.children[v])

  def __print(self, node, i=0):
    print(f'{"--" * i}{node.data}')

    arr = list(node.children.keys())
    arr.sort()

    for v in arr:
      self.__print(node.children[v], i+1)
    

hive = Hive()

n = int(rl())
for _ in range(n):
  temp = rl().split()
  hive.push(temp[1:])

hive.print()