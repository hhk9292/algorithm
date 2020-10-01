# SWEA
# [S/W 문제해결 기본] 9일차 - 중위순회
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE

for tc in range(1, 11):
    N = int(input())
    bi_tree = ['Root'] + ([None] * N)

    for _ in range(N):
        node_info = list(input().split())
        bi_tree[int(node_info[0])] = node_info[1]
    # print(bi_tree)

    i = 1
    answer = []
    while bi_tree[i] != 'Root':
        # if bi_tree[i] is None:
        #     i //= 2
        # print(i, bi_tree[i])
        if (i * 2 > N) or (bi_tree[i * 2] is None):
            if bi_tree[i] is not None:
                answer.append(bi_tree[i])
            bi_tree[i] = None
            if ((i * 2) + 1 > N) or (bi_tree[(i * 2) + 1] is None):
                i //= 2
            else:
                i = (i * 2) + 1

            continue
        else:
            i *= 2
        # print(answer)
    answer = ''.join(answer)
    print('#{} {}'.format(tc, answer))

