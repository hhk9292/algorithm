
# 2020 KAKAO BLIND
# 7. 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063

def straight_check(loc, land):
    x, y = loc
    length = len(land)
    result = []
    if (loc[0] % 2) and (loc[1] % 2 == 0):  # 가로
        if y <= length - 4 and land[x][y + 3] == 0:
            # + 방향 직진 가능
            result.append(0)

        if y >= 3 and land[x][y - 3] == 0:
            # - 방향 직진 가능
            result.append(1)

    if (loc[0] % 2 == 0) and (loc[1] % 2):  # 세로
        if x <= length - 4 and land[x + 3][y] == 0:
            # + 방향 직진 가능
            result.append(2)


        if x >= 3 and land[x - 3][y] == 0:
            # - 방향 직진 가능
            result.append(3)

    return result


def rotate_check(loc, land):
    # 회전 가능성을 보는 검사지만 평행 이동도 검사함
    x, y = loc
    length = len(land)
    result = []
    if (loc[0] % 2) and (loc[1] % 2 == 0):  # 가로
        # 아래쪽 검사
        if x <= length - 3:
            if (land[x+2][y-1] == 0) and (land[x+2][y+1] == 0):
                result.append(2)
                result.append(5)
                result.append(7)

        # 위쪽 검사
        if x >= 2:
            if (land[x-2][y-1] == 0) and (land[x-2][y+1] == 0):
                result.append(3)
                result.append(4)
                result.append(6)

    if (loc[0] % 2 == 0) and (loc[1] % 2):  # 세로
        # 오른쪽 검사
        if y <= length - 3:
            if (land[x-1][y+2] == 0) and (land[x+1][y+2] == 0):
                result.append(0)
                result.append(4)
                result.append(7)

        # 왼쪽 검사
        if y >= 2:
            if (land[x-1][y-2] == 0) and (land[x+1][y-2] == 0):
                result.append(1)
                result.append(5)
                result.append(6)
    return result


def solution(board):
    move = [
        (0, 2),
        (0, -2),
        (2, 0),
        (-2, 0),
        (-1, 1),
        (1, -1),
        (-1, -1),
        (1, 1)
    ]
    n = len(board)

    """
    가로 세로 모든 칸을 2개로 나누어서 진행
    로봇의 몸통의 위치에 따라 가로 세로가 결정되고 앞 뒤 방향성도 사라지므로
    위 사항을 고려하지 않아도 됨
    """

    land = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
    for i in range(n):
        for j in range(n):
            x, y = 2 * i + 1, 2 * j + 1
            if board[i][j] == 1:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        land[x + k][y + l] = 1

    length = len(land)
    final = {(length - 2, length - 3), (length - 3, length - 2)}
    visit = set()
    visit.add((1, 2))

    queue = []
    queue.append((1, 2, 0))
    while queue:
        cx, cy, cnt = queue.pop(0)
        land[cx][cy] = cnt
        land[cx][cy] = 0
        directs = []
        directs.extend(straight_check((cx, cy), land))
        directs.extend(rotate_check((cx, cy), land))

        for direct in directs:
            nx, ny = cx + move[direct][0], cy + move[direct][1]
            if (nx, ny) in final:
                queue = []
                break

            if (nx, ny) not in visit:
                visit.add((nx, ny))
                queue.append((nx, ny, cnt + 1))
    answer = cnt + 1
    return answer