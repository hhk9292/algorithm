# 2018 KAKAO BLIND
# [3차] 자동완성
# https://programmers.co.kr/learn/courses/30/lessons/17685
import sys
sys.setrecursionlimit(10**6 + 1)
class Node:
    def __init__(self):
        self.cnt = 1
        self.c = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        self._insert(curr, 0, word)

    def _insert(self, root, i, word):
        if i >= len(word): return
        letter = word[i]
        if letter in root.c.keys():
            root.c[letter].cnt += 1
            self._insert(root.c[letter], i+1, word)

        else:
            root.c[letter] = Node()
            self._insert(root.c[letter], i + 1, word)

    def find(self, word):
        curr = self.root
        i = 0
        while i < len(word):
            letter = word[i]
            chk = curr.c[letter]
            if chk.cnt == 1:
                i += 1
                break
            else:
                i += 1
                curr = chk
        return i


def solution(words):
    answer = 0
    trie = Trie()
    for word in words:
        trie.insert(word)

    for word in words:
        answer += trie.find(word)
    return answer

words = ['go','gone','guild']
a = solution(words)
print(a)
