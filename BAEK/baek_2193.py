# BAEK
# 이친수
# https://www.acmicpc.net/problem/2193
import sys
input = sys.stdin.readline

N = int(input())
nums = [0, 1, 1] + [-1] * (N - 2)


def pinary(N):
    if nums[N] != -1:
        return nums[N]

    temp = pinary(N-1) + pinary(N-2)
    nums[N] = temp
    return temp

print(pinary(N))