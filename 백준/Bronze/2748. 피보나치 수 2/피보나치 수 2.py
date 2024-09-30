import sys
sys.setrecursionlimit(10**6)
n_in = int(sys.stdin.readline())
n_list = [0] * (n_in + 1)

def fivo(N):
    if N == 1 or N == 2:
        return 1
    if n_list[N] != 0:
        return n_list[N]
    n_list[N] = fivo(N-1) + fivo(N-2)
    return  n_list[N]

result = fivo(n_in) 
print(result)


        