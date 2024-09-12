import math
#소수 판별 함수
def check_prime(num) -> bool:
    if num < 2:
        return False
    is_prime = True
    for test in range(2, int(math.sqrt(num))+1):
        if num%test == 0:
            is_prime = False
            break
        else:
            is_prime = True
    return is_prime

    
num = int(input())
num_list = []
for i in range(num):
    in_num = int(input())
    num_list.append(in_num)
for n in num_list:
    for num1 in range(2, n//2):
        print('n//2', n//2)
        if check_prime(num1) and check_prime(n - num1):
            print("결과", num1, n - num1)
        else:
            print('pass')
            pass