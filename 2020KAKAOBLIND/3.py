# 2020 KAKAO BLIND
# 3. 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate_key(key, n):
    """
    key 를 시계방향으로 90도 돌려서 리턴


    :param key:
    2차원 배열의 key


    :param n:
    key 의 크기


    :return:
    90도 회전한 key
    """
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1] = key[i][j]
    return temp

def check(i, j, key, n, board, m):
    """
    key 가 맞는지 확인하는 함수


    :param i:
    시작점 i 좌표


    :param j:
    시작점 j 좌표


    :param key:
    key 배열


    :param n:
    key 의 크기


    :param board:
    board 배열


    :param m:
    lock 의 크기


    :return:
    key 로 lock 을 열 수 있으면 True 아니면 False 리턴
    """
    for k in range(n):
        for l in range(n):
            # key 와 board 를 맞춰봄
            board[i+k][j+l] += key[k][l]

    # lock 을 탐색 하다가 1이 아닌 곳이 있으면 False 리턴
    for k in range(m):
        for l in range(m):
            if board[n+k-1][n+l-1] != 1:
                return False

    return True

def solution(key, lock):
    n = len(key)  # key 의 크기
    m = len(lock)  # lock 의 크기

    # key 가 lock 외부로 나갈 수 있기 때문에 최대 크기의 board 를 만든다.
    board = [[0] * (m + 2*n - 2) for _ in range(m + 2*n - 2)]
    for i in range(m):
        for j in range(m):
            board[n+i-1][n+j-1] = lock[i][j]

    # key 를 움직여가며 체크
    for i in range(n+m-1):
        for j in range(n+m-1):
            # 회전하면서 체크하므로 4번 해야한다.
            for _ in range(4):
                # 성공하면
                if check(i, j, key, n, board, m):
                    return True
                # 실패 했을 때
                else:
                    # lock 부분을 초기화 시켜준다.
                    for k in range(m):
                        for l in range(m):
                            board[n+k-1][n+l-1] = lock[k][l]
                    key = rotate_key(key, n)

    # 성공하지 못하고 여기로 나왔을 때
    return False

