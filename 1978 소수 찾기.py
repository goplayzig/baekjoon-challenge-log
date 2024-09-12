# 진짜 무조건 다시 풀어볼것. 
# 소수, 제곱근, 개념 다시 알기 

import sys
import math

counter = 0
N = int(sys.stdin.readline())
numberList = list(map(int, sys.stdin.readline().split()))

for number in numberList:
    if number < 2:
        continue  
    is_prime = True
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            is_prime = False
            break
    if is_prime:
        counter += 1

print(counter)

# import sys
# import math

# counter = 0
# N = int(sys.stdin.readline())
# numberList = list(map(int, sys.stdin.readline().split()))
# for i in range(len(numberList)):
#     number = numberList[i]
#     for x in range(2, int(math.sqrt(number)+1)):
#         if number % i != 0 and number > 2:
#             print("넘버", number)
#             counter = counter + 1
# print(counter)


# import math
# def is_prime(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#         return True

# print(is_prime(31))