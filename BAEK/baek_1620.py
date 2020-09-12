# BAEK
# 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_to_num = {}
num_to_name = []
for i in range(N):
    name = input().rstrip()
    name_to_num[name] = i + 1
    num_to_name.append(name)

for _ in range(M):
    target = input().rstrip()
    if target.isdigit():
        print(num_to_name[int(target) - 1])
    else:
        print(name_to_num[target])

