# 2029 KAKAO BLIND
# 4. 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891


def solution(food_times, k):
    n = len(food_times)
    answer = 0
    # [음식 번호, 먹는 시간]으로 묶어서 배열에 넣는다.
    foods = [[i+1, val] for i, val in enumerate(food_times)]
    foods.sort(key=lambda food: food[1])

    while n > 0:
        time = foods[0][1]
        if k - n*time < 0:
            break
        k -= n * time
        foods.pop(0)
        n -= 1
        for i in range(n):
            foods[i][1] -= time

    if k - n*time >= 0:
        answer = -1
    else:
        foods.sort(key=lambda food: food[0])
        answer = foods[k%n][0]

    return answer

