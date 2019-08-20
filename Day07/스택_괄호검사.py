# # var = '()()((()))'

# def parenthesis(x):
#     stack = []

#     for i in range(len(x)):
#         if x[i] == '(':
#             stack.append(x)
#         else: 
#             if stack == []:
#                 return '오류'
#             else:
#                 stack.pop()

#     if stack == []:
#         return '오류 없음'       
#     else:
#         return '오류'

# var1 = '()()((()))'
# var2 = '((()((((()()((()())((())))))'
# var3 = ')()()'
# var4 = '()()'
# var5 = '(())((()))((((()))'

# print(parenthesis(var1))
# print(parenthesis(var2))
# print(parenthesis(var3))
# print(parenthesis(var4))
# print(parenthesis(var5))


stack = [0] * 100
top = -1
str = '(()()))'

correct = True
for i in range(len(str)):
    if str[i] == '(':
        top += 1
        stack[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            correct = False
            break
        top -= 1

if top == -1 and correct:
    print('correct')
else:
    print('wrong')