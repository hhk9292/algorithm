# BAEK
# 테트로미노
# https://www.acmicpc.net/problem/14500

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 세로, 가로
tet = [list(map(int, input().split())) for _ in range(N)]
possible_6 = [{0, 1}, {0, 2}, {0, 5}, {1, 2}, {2, 3}, {3, 4}, {3, 5}, {4, 5}]

def check_6(x, y, dx, dy):
    if (x+dx > N) or (y+dy > M): return
    if dy > dx:  # 가로로 긴 직사각형
        chk_list = []
        for i in range(x, x+dx):
            for j in range(y, y+dy):
                chk_list.append(tet[i][j])

    else:  # 세로로 긴 직사각형
        chk_list = []
        for j in range(y, y+dy):
            for i in range(x, x+dx):
                chk_list.append(tet[i][j])

    check_sum(chk_list)

def check_sum(array):
    global ans
    for possible in possible_6:
        temp_sum = 0
        for idx in range(6):
            if idx in possible:
                continue
            else:
                temp_sum += array[idx]
        if temp_sum > ans:
            ans = temp_sum

ans = 0
for i in range(N):
    for j in range(M):
        # 직사각형 모양 체크
        check_6(i, j, 2, 3)
        check_6(i, j, 3, 2)

        # 직선 모양 체크
        if j <= M - 4:
            temp_sum = 0
            for k in range(4):
                temp_sum += tet[i][j+k]
            if temp_sum > ans:
                ans = temp_sum
        if i <= N - 4:
            temp_sum = 0
            for k in range(4):
                temp_sum += tet[i+k][j]
            if temp_sum > ans:
                ans = temp_sum

        # 정사각형 체크
        if (i <= N - 2) and (j <= M - 2):
            temp_sum = 0
            for k in range(2):
                for l in range(2):
                    temp_sum += tet[i+k][j+l]
            if temp_sum > ans:
                ans = temp_sum

print(ans)