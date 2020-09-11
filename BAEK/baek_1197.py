# BAEK
# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197

# find 함수
def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

# union 함수
def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    else:
        if r[px] > r[py]:
            p[py] = px
        elif r[px] < r[py]:
            p[px] = py
        else:
            p[py] = px
            r[px] += 1
    return

V, E = map(int, input().split())  # 정점과 간선의 개수
p = [i for i in range(V + 1)]  # 부모 배열
r = [0 for _ in range(V + 1)]  # rank 배열

graph = []
for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))  # (가중치, 출발점, 도착점)

graph.sort(key=lambda x: x[0])  # 가중치가 작은 것부터 오름차순으로 정렬

cnt = 0  # 노드의 개수를 세는 변수
mst = 0  # 가중치의 합이 들어갈 변수

for node in graph:
    (dist, start, goal) = node

    if find(start) != find(goal):
        union(start, goal)
        mst += dist
        cnt += 1

    if cnt == V-1:
        break

print(mst)

