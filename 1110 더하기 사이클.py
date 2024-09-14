import sys

N = int(sys.stdin.readline())
count = 0
x = N

while True:
    if x < 9:
        first = 0 
        second = x
    else:
        first = x // 10  
        second = x % 10  

    result = first + second
    x = (second * 10) + (result % 10)
    count += 1 
    if x == N:
        break

print(count)
