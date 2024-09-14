import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

def search(target: int) -> bool:
    pl = 0
    pr = len(N_list) - 1
    while True:
        pivot = (pl + pr) // 2
        if N_list[pivot] == target:
            return True
        elif N_list[pivot] < target:
            pl = pivot + 1
        else:
            pr = pivot - 1
        if pl > pr:
            break
    return False

for i in range(0, len(M_list)):
    if search(M_list[i]):
        print(1)
    else: 
        print(0)
