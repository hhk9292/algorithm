# 2018 KAKAO BLIND
# [1차] 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678

def time_to_num(time):
    h, m = map(int, time.split(':'))
    return (60 * h) + m

def num_to_time(num):
    h = str(num // 60)
    m = str(num % 60)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    return h + ':' + m

def is_onboard(time, buses, n, t, m):
    bus_num = max((time - 540), 0) // t
    chk = max((time - 540), 0) % t
    if chk:
        bus_num += 1
    while bus_num < n:
        if len(buses[bus_num]) < m:
            return True

        elif time < buses[bus_num][-1]:
            return True

        else:
            bus_num += 1
    return False


def solution(n, t, m, timetable):
    answer = ''
    arrivals = []
    buses = [[] for _ in range(n)]
    for time in timetable:
        arrivals.append(time_to_num(time))

    arrivals.sort()
    for arrival in arrivals:
        bus_num = max((arrival - 540), 0) // t
        chk = max((arrival - 540), 0) % t
        if chk:
            bus_num += 1
        while bus_num < n:
            if len(buses[bus_num]) < m:
                buses[bus_num].append(arrival)
                break
            else:
                bus_num += 1

    left = 0
    right = 540 + (n - 1) * t + 1
    while left <= right:
        mid = (left + right) // 2
        if is_onboard(mid, buses, n, t, m):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return num_to_time(answer)

n = 1
t = 1
m = 1
timetable = ['25:59']
a = solution(n, t, m, timetable)
print(a)