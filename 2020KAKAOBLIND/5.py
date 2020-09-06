# 2020 KAKAO BLIND
# 5. 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061


def check(elem, wall):
    x, y, kind = elem
    if kind == 0:  # 기둥
        if y == 0:  # 바닥에 설치
            return True
        if (x, y-1, 0) in wall:  # 한 칸 아래에 기둥이 있는 경우
            return True
        if (x, y, 1) in wall or (x-1, y, 1) in wall:  # 현 위치나 왼쪽에 보가 있는 경우
            return True
        return False

    else:  # 보
        if (x, y-1, 0) in wall or (x+1, y-1, 0) in wall:  # 한 칸 아래나 아래 오른쪽에 기둥이 있는 경우
            return True
        if (x-1, y, 1) in wall and (x+1, y, 1) in wall:  # 양 옆에 보가 있는 경우
            return True
        return False


def solution(n, build_frame):
    wall = set()  # 건축물이 들어갈 set
    for build in build_frame:  # build = [x좌표, y좌표, 기둥/보, 설치/삭제]
        elem = (build[0], build[1], build[2])
        if build[3] == 1:  # 설치
            # 여기에 체크 함수
            if check(elem, wall):
                wall.add(elem)
            pass
        else:
            # 여기에 체크 함수
            # 먼저 삭제 후 다른 건축물들에 대해 check 함수를 돌린다.
            wall.remove(elem)
            for other_elem in wall:
                # 다른 건축물 중 하나라도 건축이 불가능 할 경우
                # 건축물을 다시 추가한다.
                if not check(other_elem, wall):
                    wall.add(elem)
                    break

    answer = [list(elem) for elem in wall]
    answer.sort(key=lambda elem: (elem[0], elem[1], elem[2]))
    return answer
