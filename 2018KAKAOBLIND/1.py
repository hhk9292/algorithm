# 2018 KAKAO BLIND
# [1차] 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676

def get_time(time):
    h, m, s = map(float, time.split(':'))
    return 1000 * (3600 * h + 60 * m + s)

def get_advert_num(time, time_table):
    duration = 999
    start = time[0]
    end = time[1]

    s_num = 0
    e_num = 0

    for adv in time_table:
        # start check
        if (adv[1] >= start) and (adv[0] <= start + duration):
            s_num += 1

        # end check
        if (adv[1] >= end) and (adv[0] <= end + duration):
            e_num += 1

    return max(s_num, e_num)

def solution(lines):
    time_table = []
    for line in lines:
        # line => 2016-90-15 hh:mm:ss.sss Ts
        day, time, duration = line.split()
        end = get_time(time)
        duration = float(duration.rstrip('s')) * 1000
        start = end - duration + 1
        time_table.append((int(start), int(end)))

    answer = 0
    for adv in time_table:
        answer = max(get_advert_num(adv, time_table), answer)
    return answer

