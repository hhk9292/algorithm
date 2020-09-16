# SWEA
# [S/W 문제해결 응용] 9일차 - 달란트2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18R8FKIvoCFAZN&categoryId=AV18R8FKIvoCFAZN&categoryType=CODE

T = int(input())  # 전체 테스크 케이스

for tc in range(1, T+1):
    N, P = map(int, input().split())  # 달란트, 묶음의 수
    # N//P로 최대한 나누고 남는 부분에 1씩 더해준다
    # 예를들어 10, 4 일 경우 2 2 2 2 하고 2가 남기 때문에 2 2 2+1 2+1 이런식으로 만들어준다
    # 나누어 떨어지는 경우에는 (N//P) ** P
    result = (N//P) ** (P-N%P)
    for _ in range(N%P):
        result *= (N//P + 1)
    print("#{} {}".format(tc, result))