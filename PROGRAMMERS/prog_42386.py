# PROGRAMMERS STACK/QUEUE
# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42386

def solution(progresses, speeds):
    answer = []
    cnt = 0
    i = 0
    while i < len(progresses):
        progress = progresses[i]
        speed = speeds[i]
        if progress >= 100:
            cnt += 1
            i += 1
            continue
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0

            remainder = (100 - progress) % speed
            cycle = (100 - progress) // speed
            if remainder != 0:
                cycle += 1

            for j in range(i, len(progresses)):
                progresses[j] += speeds[j] * cycle

    answer.append(cnt)
    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
a = solution(progresses, speeds)
print(a)