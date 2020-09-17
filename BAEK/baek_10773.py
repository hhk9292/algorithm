# BAEK
# 제로
# https://www.acmicpc.net/problem/10773

n = int(input())
nums = [0]  # 숫자가 다 지워지는 경우 대비
for _ in range(n):
    temp = int(input())
    if temp == 0:
        nums.pop()
    else:
        nums.append(temp)
print(sum(nums))

