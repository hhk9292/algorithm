# BAEK
# 퇴사 2
# https://www.acmicpc.net/problem/15486

import sys
input = sys.stdin.readline

N = int(input().rstrip())
days = []
pays = []

for i in range(N):
    day, pay = map(int, input().split())
    days.append(day)
    pays.append(pay)

max_pay = [0] * (N+1)
for i in range(N):
    if i + days[i] <= N:
        max_pay[i + days[i]] = max(max_pay[i + days[i]], pays[i] + max_pay[i])

    max_pay[i + 1] = max(max_pay[i], max_pay[i+1])

print(max_pay[N])