# SWEA
# [SW Test 샘플문제] 프로세서 연결하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

from copy import deepcopy

directions = {
    1: (-1, 0),  # 상
    2: (0, 1),   # 우
    3: (1, 0),   # 하
    4: (0, -1)   # 좌
}

def direction_check(i, j, d):
    (di, dj) = directions[d]
    ni, nj = i + di, j + dj
    while (0 <= ni < N) and (0 <= nj < N):
        if cpu[ni][nj] != 0:
            return False
        ni, nj = ni + di, nj + dj

    return True

def connect_wire(i, j, d):
    (di, dj) = directions[d]
    ni, nj = i + di, j + dj
    cnt = 0
    while (0 <= ni < N) and (0 <= nj < N):
        cpu[ni][nj] = 1
        cnt += 1
        ni, nj = ni + di, nj + dj
    return cnt


def dfs(i, core_num, wire_len):
    global max_core, min_wire, cpu
    if i == n:
        if core_num > max_core:
            max_core = core_num
            min_wire = wire_len

        elif core_num == max_core:
            if wire_len < min_wire:
                min_wire = wire_len
        return

    if core_num + n - i < max_core:
        return

    core = cores_list[i]
    core_directions = cores_dict[core]

    for core_direct in core_directions:
        if core_direct == 0:
            dfs(i+1, core_num, wire_len)
        else:
            ci, cj = core
            if direction_check(ci, cj, core_direct):
                temp_cpu = deepcopy(cpu)
                wire = connect_wire(ci, cj, core_direct)
                dfs(i+1, core_num + 1, wire_len + wire)
                cpu = temp_cpu
    return






total_tc = int(input())
for tc in range(total_tc):
    cores_dict = {}
    cores_list = []
    N = int(input())
    cpu = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, N-1):
            if cpu[i][j] == 1:
                cores_dict[(i, j)] = [0]  # 0 => 연결 안함
                cores_list.append((i, j))
                for direction in directions:
                    if direction_check(i, j, direction):
                        cores_dict[(i, j)].append(direction)
    n = len(cores_list)
    max_core = 0
    min_wire = float('inf')
    dfs(0, 0, 0)
    print('#{} {}'.format(tc+1, min_wire))