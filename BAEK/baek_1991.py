# BAEK
# 트리 순회
# https://www.acmicpc.net/problem/1991

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data=None):
        self.data = data
        self.l = None
        self.r = None

N = int(input())
nodes = [None] * N
for _ in range(N):
    d, l, r = input().rstrip().split()
    if nodes[ord(d) - 65] is None:
        nodes[ord(d) - 65] = Node(d)

    if l != '.':
        curr = nodes[ord(d) - 65]
        if nodes[ord(l) - 65] is None:
            nodes[ord(l) - 65] = Node(l)
        curr.l = nodes[ord(l) - 65]

    if r != '.':
        curr = nodes[ord(d) - 65]
        if nodes[ord(r) - 65] is None:
            nodes[ord(r) - 65] = Node(r)
        curr.r = nodes[ord(r) - 65]

preorder = []
inorder = []
postorder = []

def search(root):
    if root is None:
        return

    preorder.append(root.data)
    search(root.l)
    inorder.append(root.data)
    search(root.r)
    postorder.append(root.data)


search(nodes[0])
print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))