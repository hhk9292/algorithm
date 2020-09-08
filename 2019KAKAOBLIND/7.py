# 2029 KAKAO BLIND
# 7. 블록게임
# https://programmers.co.kr/learn/courses/30/lessons/42894

def rec_check(board, n, x, dx, y, dy):
    """직사강형 형태를 검사해서 가능성이 있는지 검사"""
    # 검사하는 직사각형이 보드를 벗어나면 False
    if (x + dx > n) or (y + dy > n): return False
    # 3 * 2 혹은 2 * 3 직사각형 내부를 탐색
    _zeros = 0
    num_check = set()
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            if board[i][j] == 0:
                _zeros += 1
                if _zeros >= 3:
                    return False
            else:
                num_check.add(board[i][j])
                if len(num_check) >= 2:
                    return False
    return True

def tetris(board, n, x, dx, y, dy):
    """테트리스가 가능한 지 확인"""
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            if board[i][j] == 0:
                for k in range(i + 1):
                    if board[k][j] != 0:
                        return False

    for i in range(x, x + dx):
        for j in range(y, y + dy):
            board[i][j] = 0

    return True


def solution(board):
    answer = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if rec_check(board, n, i, 2, j, 3):
                if tetris(board, n, i, 2, j, 3):
                    answer += 1
            if rec_check(board, n, i, 3, j, 2):
                if tetris(board, n, i, 3, j, 2):
                    answer += 1
        for j in range(n-1, -1, -1):
            if rec_check(board, n, i, 2, j, 3):
                if tetris(board, n, i, 2, j, 3):
                    answer += 1
            if rec_check(board, n, i, 3, j, 2):
                if tetris(board, n, i, 3, j, 2):
                    answer += 1

    return answer