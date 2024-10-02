import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(sys.stdin.readline())

def count_binary_sequences(n):
    MOD = 15746

    dp = [0] * (n + 1)
    
    dp[1] = 1
    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        
    return dp[n]

print(count_binary_sequences(N))
# 아니 이러면 결국 피보나츠의 수열 문제가 아닌가 ... 

    



