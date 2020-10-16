# PROGRAMMERS LEVEL 3
# 멀리 뛰기
# https://programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    if n < 3:
        return n
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        i = 3
        while i <= n:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
            i += 1
        return dp[n] 

