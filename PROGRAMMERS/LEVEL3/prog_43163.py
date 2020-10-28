# PROGRAMMERS LEVEL 3
# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    answer = 0
    word_length = len(begin)
    max_try = len(words) + 1
    queue = [begin]
    checked = set()
    found = False
    while queue:
        answer += 1
        temp = []
        begin = queue.pop(0)
        for word in words:
            if word in checked:
                continue
            cnt = 0
            for i in range(word_length):
                if begin[i] != word[i]:
                    cnt += 1
                    if cnt >= 2:
                        break

            if cnt == 1:
                if word == target:
                    found = True
                    break
                temp.append(word)
                checked.add(word)
        if found:
            break
        queue = temp
    if not found:
        answer = 0
    return answer



begin = 'abcdef'
target = 'fedcba'
words = ['abcdea', 'abcdba', 'abccba', 'abdcba', 'aedcba']
a = solution(begin, target, words)
print(a)