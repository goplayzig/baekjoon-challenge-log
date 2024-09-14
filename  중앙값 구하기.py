# 반복 과정에서 조건 판단하기 3 (미해결 )
# print('*를 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))
# w = int(input('몇 개마다 줄바꿈할까요?: '))

# for i in range(n):
#     print('*',end="")
#     if i % w == w - 1:
#         print()

# if n % w:
#     print()




#반복 과정에서 조건 판단하기 

# n = int(input())

# for _ in range(n // 2):
#     print('+-', end='')

# if n % 2:
#     print('+', end='')


# 1부터 n 까지의 덧셈

# n = int(input('숫자 입력'))
# sum = 0 

# for i in range(0,n+2):
#     sum += i

# print(f'1부터 {n}까지 더한값은 {sum} 입니다.')

#중앙값 구하기
# def med3(a, b, c):
#     if a >= b:
#         if b >= c:
#             return b 
#         elif a <= c:
#             return a
#         else:
#             return 
#     elif a > c:
#         return a
#     elif b > c:
#         return c
#     else:
#         return b 
    
# a = int(input('첫번째 값:'))
# b = int(input('두번째 값:'))
# c = int(input('세번째 값:'))
# print(f'중앙값은 {med3(a,b,c)} 입니다.')
 