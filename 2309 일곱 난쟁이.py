import sys

heigh = []
total = 0 

for i in range(9):
    input_val = int(sys.stdin.readline()) 
    heigh.append(input_val)
    total += input_val

remain = total - 100
found = False

for x in range(len(heigh)):
    pivot = heigh[x]
    for n in range(x + 1, len(heigh)):  # x 이후의 인덱스만 탐색
        if remain - pivot - heigh[n] == 0:
            heigh.pop(n)  # 먼저 뒤쪽 인덱스 삭제 (먼저 삭제해야 인덱스 문제가 없음)
            heigh.pop(x)  # 그 다음 앞쪽 인덱스 삭제
            found = True
            heigh.sort()  
            break
    if found:
        break

for i in range(7):
    print(heigh[i])