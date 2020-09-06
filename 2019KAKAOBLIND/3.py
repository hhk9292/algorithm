# 2029 KAKAO BLIND
# 3. 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

def check(relation, key):
    """후보키가 될 수 있는지 검사"""
    temp = set()
    for row in relation:
        candidate = tuple(row[i] for i in key)
        if candidate in temp:
            return False
        else:
            temp.add(candidate)
    return True

def solution(relation):
    # 후보키의 조합을 만들기 위해 combinations 사용
    from itertools import combinations
    # 후보키가 저장 되는 리스트
    candidate_keys = []
    n = len(relation[0])  # column 의 개수
    # 후보키는 1 개부터 n 개까지 나올 수 있음
    for l in range(1, n+1):
        keys = combinations(range(n), l)
        for key in keys:
            set_keys = set(key)
            flag = True
            # 후보키 리스트에 저장되어 있는 후보키들과 비교
            for candidate_key in candidate_keys:
                # 현재 검사하려는 키가 이미 등록된 후보키를 포함하고 있으면 반복문 탈출
                if candidate_key & set_keys == candidate_key:
                    flag = False
                    break
            if not flag:
                continue
            # 후보키 리스트와 상관 없는 키는 후보키가 될 수 있는지 검사
            if check(relation, key):
                candidate_keys.append(set_keys)
    answer = len(candidate_keys)
    return answer
