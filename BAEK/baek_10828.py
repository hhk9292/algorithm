# BAEK
# 스택
# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command_line = input().split()
    if len(command_line) == 2:
        stack.append(command_line[1])
    else:
        command = command_line[0]
        if command == 'pop':
            if len(stack) == 0:
                print('-1')
            else:
                print(stack.pop())

        elif command == 'size':
            print(len(stack))

        elif command == 'empty':
            if len(stack) == 0:
                print('1')
            else:
                print('0')
        else:
            if len(stack) == 0:
                print('-1')
            else:
                print(stack[-1])