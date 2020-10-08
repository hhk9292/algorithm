# 2018 KAKAO BLIND
# [1차] 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

def sq_check(i, j, board):
    temp = board[i][j]
    for di in range(2):
        for dj in range(2):
            if board[i + di][j + dj] != temp:
                return False
    return True

def chk_list(m, n, board):
    temp = []
    for i in range(n - 1):
        for j in range(m - 1):
            if board[i][j] == '':
                continue
            else:
                if sq_check(i, j, board):
                    temp.append((i, j))
    return temp


def solution(m, n, board):
    answer = 0
    for row in board:
        row = list(row)
    board = list(map(list, zip(*board)))
    check_list = chk_list(m, n, board)
    while check_list:
        check_set = set()
        for check_point in check_list:
            x, y = check_point
            for dx in range(2):
                for dy in range(2):
                    if board[x + dx][y + dy] == '':
                        continue
                    else:
                        board[x + dx][y + dy] = ''
                        answer += 1
                        check_set.add(x + dx)

        for check_x in check_set:
            lane = board[check_x]
            cnt = 0
            for cx in range(m-1, -1, -1):
                if lane[cx] == '':
                    lane.pop(cx)
                    cnt += 1
            lane = [''] * cnt + lane
            board[check_x] = lane
        check_list = chk_list(m, n, board)

    return answer


board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
a = solution(6, 6, board)
print(a)