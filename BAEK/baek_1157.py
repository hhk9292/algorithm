# BAEK
# 단어 공부
# https://www.acmicpc.net/problem/1157

import sys
input = sys.stdin.readline

word = input().rstrip()
counting = [0] * 26  # 알파벳은 26개
for letter in word:
    if letter >= 'a':
        counting[ord(letter) - 97] += 1  # a 의 아스키 코드는 97
    else:
        counting[ord(letter) - 65] += 1  # A의 아스키 코드는 65

max_num = 0
idx = -1
for i in range(26):
    if counting[i] > max_num:
        max_num = counting[i]
        idx = i

result = ''
if counting.count(max_num) >= 2:
    result = '?'
else:
    result = chr(idx + 65)

print(result)