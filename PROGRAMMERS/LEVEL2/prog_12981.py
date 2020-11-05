# PROGRAMMERS LEVEL 2
# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981


def solution(n, words):
    answer = [0, 0]
    prev = ''
    check = set()
    for i, word in enumerate(words):
        if i == 0:
            check.add(word)
        else:
            if (word in check) or (prev[-1] != word[0]) or (len(word) == 1):
                if (i+1) % n:
                    answer = [(i+1) % n, ((i+1)//n) + 1]
                else:
                    answer = [n, (i+1)//n]
                break
            else:
                check.add(word)
        prev = word
    return answer

n = 2
words = ['qwe', 'eqwe', 'eqwe']
answer = solution(n, words)
print(answer)