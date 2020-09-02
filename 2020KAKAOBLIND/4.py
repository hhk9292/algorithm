# 2020 KAKAO BLIND
# 4. 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

class Node(object):
    """
    Node for Trie
    """

    def __init__(self):
        """
        노드가 생성 될 때 실행되는 함수
        """

        self.count = 0  # 현재 노드를 거쳐가는 단어의 수
        self.children = dict()  # 자식 노드


class Trie(object):
    """
    Trie
    """

    def __init__(self):
        """
        Trie 구조가 생성될 때 실행되는 함수
        """

        new_node = Node()
        self.header = new_node


    def insert(self, word):
        """
        단어를 Trie 구조에 저장하는 함수

        :param word:
        저장하려는 단어
        """

        # Trie 의 header 를 시작점으로 잡는다.
        curr_node = self.header
        for letter in word:  # 단어의 문자를 순회하면서
            curr_node.count += 1  # 이 노드를 거쳐간 단어의 개수를 증가시켜준다.
            # 자식 노드에 문자가 있으면 그 노드로 이동
            if letter in curr_node.children.keys():
                curr_node = curr_node.children[letter]
            # 없으면 새로운 노드를 만들어 저장 후 이동
            else:
                new_node = Node()
                curr_node.children[letter] = new_node
                curr_node = new_node
        # 제일 마지막 노드의 카운트도 1 증가
        curr_node.count += 1

    def search(self, word):
        """
        Trie 구조에서 원하는 단어가 있는지 확인


        :param word:
        찾으려는 단어


        :return:
        찾으려는 단어이거나, 그 단어로 시작하는 단어들의 개수를 리턴
        """

        # Trie 의 header 를 시작점으로 잡는다.
        curr_node = self.header
        for letter in word:
            if letter not in curr_node.children.keys():
                return 0
            else:
                curr_node = curr_node.children[letter]
        return curr_node.count


def solution(words, queries):
    # 키워드의 길이가 1이상 10000 이하이므로 10001짜리 리스트를 2개 만든다.
    # 리스트를 2개 만드는 이유는 와일드카드가 접두사로 오는 경우 뒤집어서 찾아야 하기 때문

    normal_tries = [Trie() for _ in range(10001)]
    backward_tries = [Trie() for _ in range(10001)]

    # 정방향 단어와 역방향 단어 모두 각 길이에 맞는 Trie 에 저장
    for word in words:
        n = len(word)
        normal_tries[n].insert(word)
        backward_tries[n].insert(word[::-1])

    answer = []
    for query in queries:
        n = len(query)
        # 와일드카드 문자로 시작하는 단어는 ?를 없애고 뒤집어준다.
        if query.startswith('?'):
            query = query.replace('?', '')
            answer.append(backward_tries[n].search(query[::-1]))
        # 와일드카드 문자가 뒤에 있으면 ?만 없애준다.
        else:
            query = query.replace('?', '')
            answer.append(normal_tries[n].search(query))

    return answer
