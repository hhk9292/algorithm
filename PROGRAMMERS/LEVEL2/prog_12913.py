# PROGRAMMERS LEVEL 2
# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for i, row in enumerate(land):
        if i == 0:
            continue
        else:
            for j in range(4):
                land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])

# test case
# answer = 16
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
answer = solution(land)
print(answer)