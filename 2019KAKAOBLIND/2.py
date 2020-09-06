# 2029 KAKAO BLIND
# 2. 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def accum_list(N, stages):
    """인덱스가 낮아지는 쪽으로 값이 합쳐지는 누적 배열 리턴"""
    temp = [0] * (N + 2)  # 인덱스가 N + 1 까지 있어야 하기 때문
    for stage in stages:
        temp[stage] += 1

    for i in range(N, 0, -1):  # N 부터 1 까지 이동하면서 누적
        temp[i] += temp[i+1]

    return temp

def solution(N, stages):
    # 각 인덱스에 해당하는 스테이지에 도착한 인원이 저장된다.
    numbers = accum_list(N, stages)
    answer = [0] * (N)
    for i in range(1, N + 1):
        if numbers[i] == 0:  # 도달한 인원이 0 이면
            answer[i - 1] = 0  # 실패율 0
        else:
            # 현재 스테이지에 있는 인원 = 현재 스테이지를 도달한 인원 - 다음 스테이지를 도달한 인원
            answer[i - 1] = (numbers[i] - numbers[i+1]) / numbers[i]

    answer = list(enumerate(answer))
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [i + 1 for (i, rate) in answer]
    return answer
