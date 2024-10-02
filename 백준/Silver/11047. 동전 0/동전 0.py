import sys

coin_types = []
result = 0
counter = 0
N, K = map(int, sys.stdin.readline().split())
for i in range(N):
    coin_type = int(sys.stdin.readline())
    coin_types.append(coin_type)

coin_types.reverse()
for coin in coin_types:
    result += K // coin
    K = K % coin

print(result)

    
    
