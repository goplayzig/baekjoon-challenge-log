import sys
def hanoi(no: int, start: int, end: int) -> None:
    if no == 1: 
        print(start, end) # 가장 작은 원판을 1 번 기둥에서 목표 기둥으로 옮기기 위함
    else:
        hanoi(no-1, start, 6-start-end) # 임시 기둥으로 옮기기 위함
        print(start, end) # 옮기는 print
        hanoi(no-1, 6-start-end, end) # 목표기둥으로 옮기기 위한 

    
a = int(sys.stdin.readline())
print(2 ** a - 1)
if a <= 20:
    hanoi(a, 1, 3)
    



# import sys
# def hanoi(no: int, x: int, y: int) -> None:

#     if no > 1:
#         hanoi(no-1, x, 6-x-y)

#     if no < 20 :
#         print(f'원반 [{no}]을 {x}기둥에서 {y}기둥으로 옮깁니다.')

#     if no > 1:
#         hanoi(no-1, 6-x-y, y)
    
# n = int(sys.stdin.readline())
# count = 2 ** n - 1
# print(count)
# hanoi(n, 1, 3)

