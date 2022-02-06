# BAEK
# 가운데를 말해요
# https://www.acmicpc.net/problem/1655
import sys
rl = sys.stdin.readline

import heapq

n = int(rl())
min_heap = []
max_heap = []

answer = []

for _ in range(n):

  num = int(rl())
  
  min_heap_length = len(min_heap)
  max_heap_length = len(max_heap)

  if max_heap_length == min_heap_length:
    heapq.heappush(max_heap, (-num, num))
  else:
    heapq.heappush(min_heap, (num, num))

  if (min_heap) and (min_heap[0][1] < max_heap[0][1]):
    num_from_max = heapq.heappop(max_heap)[1]
    num_from_min = heapq.heappop(min_heap)[1]

    heapq.heappush(min_heap, (num_from_max, num_from_max))
    heapq.heappush(max_heap, (-num_from_min, num_from_min))
  
  answer.append(max_heap[0][1])



for num in answer:
  print(num)