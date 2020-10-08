# 2018 KAKAO BLIND
# [1차] 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    queue = [None] * cacheSize
    for city in cities:
        # hit
        for i in range(cacheSize):
            if city == queue[i]:
                queue.append(queue.pop(i))
                answer += 1
                break

        else:
            # miss
            if cacheSize >= 1:
                queue.pop(0)
                queue.append(city)
            answer += 5

    return answer


cacheSize = 0
citis = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
a = solution(cacheSize, citis)
print(a)