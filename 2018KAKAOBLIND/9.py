# 2018 KAKAO BLIND
# [3차] 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684

dictionary = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def solution(msg):
    answer = []
    i = 0
    jump = 0
    length = 26
    while i < len(msg):
        j = 1
        while i + j <= len(msg):
            target = msg[i: i+j]
            if target in dictionary.keys():
                chk = dictionary[target]
                j += 1
                continue

            else:
                answer.append(chk)
                dictionary[target] = length + 1
                length += 1
                jump = j - 1
                break

        if i + j > len(msg):
            break
        i += jump
    answer.append(chk)
    return answer
a = solution('ABABABABABABABAB')
print(a)