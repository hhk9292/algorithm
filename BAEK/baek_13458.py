# BAEK
# 시험 감독
# https://www.acmicpc.net/problem/13458
import sys
import math
input = sys.stdin.readline

N = int(input().rstrip())
testees = list(map(int, input().split()))
B, C = map(int, input().split())
testers = N

for testee in testees:
    testers += math.ceil(max((testee - B), 0) / C)

print(testers)