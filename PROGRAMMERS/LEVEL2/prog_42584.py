# PROGRAMMERS LEVEL 2
# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42574

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        if len(stack) == 0:
            stack.append((i, price))
        else:
            if price >= stack[-1][1]:
                stack.append((i, price))
            else:
                while (len(stack) > 0) and (price < stack[-1][1]):
                    idx = stack.pop()[0]
                    answer[idx] = i - idx
                stack.append((i, price))
    for idx, price in stack:
        answer[idx] = i - idx
    return answer

prices = [1, 2, 3, 2, 3]
answer = solution(prices)
print(answer)