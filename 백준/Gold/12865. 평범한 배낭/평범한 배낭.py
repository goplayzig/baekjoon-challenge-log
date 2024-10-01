import sys

# 입력받기
n, k = map(int, sys.stdin.readline().split())  
items = []*(n+1)        # 물건의 무게와 가치를 넣을 리스트
items.append([0,0])     # 첫 번째 인덱스에 [0, 0]을 추가해 더미값을 넣음 (물건이 없는 경우)

for i in range(n):
    item = list(map(int, sys.stdin.readline().split()))  # 각 물건의 무게와 가치를 입력받아 리스트에 추가
    items.append(item) 

# DP 테이블 초기화
dp = [[0] * (k+1) for i in range(n+1)]  # DP 테이블: 물건 수와 배낭의 무게에 따른 최대 가치를 저장하는 2차원 리스트

# DP 알고리즘
for i in range(1, n+1):              # 1번째 물건부터 n번째 물건까지 순회
    for j in range(1, k+1):          # 배낭의 무게 1부터 최대 무게 k까지 순회
        if j < items[i][0]:          # 배낭의 허용 무게(j)가 현재 물건의 무게보다 작다면
            dp[i][j] = dp[i-1][j]    # 현재 물건을 넣을 수 없으므로, 이전 물건까지의 최대 가치 그대로 유지
        else:
            dp[i][j] = max(           # 두 가지 선택 중 더 큰 값을 선택
                items[i][1] + dp[i-1][j - items[i][0]],  # 현재 물건을 배낭에 넣은 경우의 가치
                dp[i-1][j]                               # 현재 물건을 넣지 않은 경우의 가치
            )

# 결과 출력: n번째 물건까지 고려했을 때 배낭의 최대 무게가 k일 때 얻을 수 있는 최대 가치
print(dp[n][k])
