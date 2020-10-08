# 2018 KAKAO BLIND
# [1차] 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17681

def num_to_hash(n, num):
    temp = ''
    while len(temp) < n:
        if num % 2:
            temp = '#' + temp
        else:
            temp = ' ' + temp
        num = num // 2
    return temp


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = arr1[i] | arr2[i]
        answer.append(num_to_hash(n, num))

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
a = solution(n, arr1, arr2)
print(a)