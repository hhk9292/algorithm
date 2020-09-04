# 2020 KAKAO BLIND
# 6. 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

def check(friends, wall, dist):
    """
    친구와 외벽 상태를 입력받아 점검 할 수 있는지 반환


    :param friends:
    점검하러 가는 친구들의 순서 배열


    :param wall:
    외벽 상태 배열


    :param dist:
    친구들이 한번에 체크할 수 있는 거리


    :return:
    모든 외벽을 점검할 수 있으면 True 못하면 False
    """

    i = 0  # 점검 하려는 외벽의 인덱스

    for friend in friends:
        f = wall[i] + dist[friend]  # 점검할 수 있는 최장 거리 외벽
        if f >= wall[-1]:  # 모든 외벽을 점검하면
            return True

        else:
            # 점검할 외벽을 찾아서 이동
            for j in range(i, len(wall)):
                if wall[j] > f:
                    i = j
                    break


def solution(n, weak, dist):
    # 친구들의 순서를 정하기 위해 permutations 이용
    from itertools import permutations
    flag = True
    # 점검하러 가는 친구들의 수
    for friends_number in range(1, len(dist)+1):
        # 그 수를 가지고 순서 정하기
        friends_permu = permutations(range(len(dist)), friends_number)
        for friends in friends_permu:
            # 원형 외벽이기 때문에 배열을 돌려가며 해야함
            for i in range(len(weak)):
                left = weak[:i]
                right = weak[i:]
                wall = right + [elem + n for elem in left]
                if check(friends, wall, dist):
                    answer = friends_number
                    flag = False
                    break

            if not flag:
                break

        if not flag:
            break

    else:
        answer = -1

    return answer