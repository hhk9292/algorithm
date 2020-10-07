# 2019 KAKAO INTERN
# 1. 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    board = list(map(list, zip(*board)))
    bucket = []
    for move in moves:
        lane = board[move - 1]
        crane = -1
        for i in range(len(lane)):
            if lane[i] != 0:
                crane = lane[i]
                lane[i] = 0
                break

        # 인형 없을 때
        if crane == -1:
            continue
        else:
            # bucket이 비어있으면
            if len(bucket) == 0:
                bucket.append(crane)
            else:
                # bucket의 가장 마지막 인형 체크
                if crane == bucket[-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(crane)
    return answer

answer = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(answer)