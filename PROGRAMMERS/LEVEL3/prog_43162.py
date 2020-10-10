# PROGRAMMERS LEVEL 3
# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    network = set()
    for i in range(n):
        if i in network:
            continue
        else:
            answer += 1
            queue = [i]
            network.add(i)
            while queue:
                x = queue.pop(0)
                for j in range(n):
                    if (x != j) and (j not in network) and (computers[x][j] == 1):
                        queue.append(j)
                        network.add(j)

    return answer



n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
a = solution(n, computers)
print(a)