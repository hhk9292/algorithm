# SWEA
# 구독자 전쟁
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXMCXV_qVgkDFAWv&categoryId=AXMCXV_qVgkDFAWv&categoryType=CODE

total_tc = int(input())
for tc in range(total_tc):
    N, P, T = map(int, input().split())
    print('#{} {} {}'.format(tc+1, min(P, T), max(P + T - N, 0)))

