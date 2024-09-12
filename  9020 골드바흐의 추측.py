import sys
import math

T = int(sys.stdin.readline())
numbers = [] #input한 넘버값들의 List

# 소수인지 확인하는 함수 
def isPrime(n) -> bool:
    if n < 2:
        return False  
    is_prime = True
    for x in range(2, int(math.sqrt(n)) + 1):
        if n % x == 0:
            is_prime = False
            break
    return is_prime

for b in range(T):
    input = int(sys.stdin.readline())
    numbers.append(input)

for i in range(len(numbers)): 
    number = numbers[i]
    a = int(number / 2)
    b = int(number / 2)
    if isPrime(a) and isPrime(b):
        print(a, b)
    else:
        while a > 1:
            if isPrime(a) and isPrime(b):
                print(a, b)
                break  
            a -= 1  
            b += 1 