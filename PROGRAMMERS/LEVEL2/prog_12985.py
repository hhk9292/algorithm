# PROGRAMMERS LEVEL 2
# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def num_to_2(n):
    result = 0
    while n > 1:
        result += 1
        n //= 2

    return result


def solution(n, a, b):
    answer = num_to_2(n)
    # 항상 a < b 로 시작
    if a > b:
        a, b = b, a

    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2

        if a > mid:
            left = mid + 1
            answer -= 1
            continue

        else:
            if b > mid:
                break
            else:
                right = mid - 1
                answer -= 1
                continue

    return answer

print(solution(8, 4, 7))