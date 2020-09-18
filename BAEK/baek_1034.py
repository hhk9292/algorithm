# BAEK
# 램프
# https://www.acmicpc.net/problem/1034
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lamps = []
for _ in range(N):
    s = input().rstrip('\n')
    lamps.append(s)

K = int(input().rstrip('\n'))

possible = {}
for i in range(N):
    zeros = 0
    row = lamps[i]
    switches = []
    for j in range(M):
        if row[j] == '0':
            zeros += 1
            switches.append(j)
            if zeros > K:
                break
    else:
        if (K - zeros) % 2 == 0:
            switches = tuple(switches)
            if switches in possible.keys():
                possible[switches] += 1
            else:
                possible[switches] = 1

result = [v for k, v in possible.items()]
result.append(0)
print(max(result))