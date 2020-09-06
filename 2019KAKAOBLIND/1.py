# 2029 KAKAO BLIND
# 1. 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    # uid 를 key 로 하고 name 을 value 로 하는 딕셔너리
    names = {}
    temp = []
    for event in record:
        # 각 event 를 공백을 기준으로 나눈다.
        event = event.split(" ")  # ex) ['Enter', 'uid1234', 'Muzi']
        if event[0] == 'Enter':
            temp.append([event[1], "님이 들어왔습니다."])
            names[event[1]] = event[2]
        elif event[0] == 'Leave':
            temp.append([event[1], "님이 나갔습니다."])
        else:
            names[event[1]] = event[2]

    answer = []
    for ans in temp:
        ans[0] = names[ans[0]]
        ans = ''.join(ans)
        answer.append(ans)

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])