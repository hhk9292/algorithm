# 2029 KAKAO BLIND
# 5. 길 찾기 게임
# https://programmers.co.kr/learn/courses/30/lessons/42892

class Node:
    def __init__(self, node):
        self.data = node[2]
        self.x = node[0]
        self.l = None
        self.r = None


class BiTree:
    def __init__(self):
        self.cnt = 0
        self.root = None

    def insert(self, node):
        new_node = Node(node)
        if self.cnt == 0:
            self.root = new_node
        else:
            self._insert_value(self.root, new_node)
        self.cnt += 1

    def _insert_value(self, root, node):
        if node.x > root.x:
            if root.r is not None:
                self._insert_value(root.r, node)
            else:
                root.r = node
        else:
            if root.l is not None:
                self._insert_value(root.l, node)
            else:
                root.l = node
        return

    def search(self, pre):
        temp = []
        node = self.root
        if pre == True:
            result = self._preorder(node, temp)
        else:
            result = self._postorder(node, temp)
        return result

    def _preorder(self, node, temp):
        if node == None:
            return
        temp.append(node.data)
        self._preorder(node.l, temp)
        self._preorder(node.r, temp)
        return temp

    def _postorder(self, node, temp):
        if node == None:
            return
        self._postorder(node.l, temp)
        self._postorder(node.r, temp)
        temp.append(node.data)
        return temp

def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10 ** 6)

    value = 1
    for node in nodeinfo:
        node.append(value)
        value += 1
    nodeinfo.sort(key=lambda node: -node[1])

    tree = BiTree()
    for node in nodeinfo:
        tree.insert(node)

    answer = []
    answer.append(tree.search(pre=True))
    answer.append(tree.search(pre=False))
    return answer
