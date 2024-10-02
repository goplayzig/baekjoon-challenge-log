import sys 

input = lambda: sys.stdin.readline().rstrip()

T = int(input())
result_count = []

for _ in range(T):
    ranks = []
    N = int(input())
    for _ in range(N):
        paper_rank, interview_rank = map(int, input().split())
        ranks.append([paper_rank, interview_rank])
    ranks.sort()
    count = 1
    top_rank = ranks[0][1]
    
    for i in range(1, N):
        if ranks[i][1] < top_rank:
            count += 1
            top_rank = ranks[i][1]
    result_count.append(count)



for solve in result_count:
    print(solve)