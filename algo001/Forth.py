import sys
sys.stdin = open("4874input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    code = input().split()
    stack = []
    for i in code:
        if i == '+' or i == '*' or i == '/' or i == '-':
            
