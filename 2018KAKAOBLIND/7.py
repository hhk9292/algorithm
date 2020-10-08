# 2018 KAKAO BLIND
# [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re
num_check = re.compile('[0-9]')
bon_check = re.compile('[A-Z]')

def solution(dartResult):
    answer = []
    score = 0
    for i in range(len(dartResult)):
        letter = dartResult[i]
        # 숫자일 경우
        if bool(num_check.match(letter)):
            if letter == '0':
                if i == 0:
                    score = 0
                else:
                    if dartResult[i-1] == '1':
                        score = 10
                    else:
                        score = 0
            else:
                score = int(letter)

        # 문자일 경우
        elif bool(bon_check.match(letter)):
            if letter == 'D':
                score = score ** 2

            elif letter == 'T':
                score = score ** 3

            answer.append(score)

        # 특수문자
        else:
            if letter == '#':
                answer[-1] *= -1

            else:
                if len(answer) >= 2:
                    answer[-2] *= 2
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2

    return sum(answer)


dartResult = '1T2D3D#'
a = solution(dartResult)
print(a)