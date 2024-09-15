import sys

def get_wood_length(trees, height):
    total = 0 
    for tree in trees: 
        if tree > height:
            total += tree - height
    return total

def find_max_saw_height(trees, M):
    start = 0  # 스타트는 0 부터
    end = max(trees) #  끝
    result = 0

    while start <= end:
        mid = (start + end) // 2
        wood = get_wood_length(trees, mid)

        if wood >= M:
            result = mid
            start = mid + 1
        else:
            end = mid -1

    return result

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
max_height = find_max_saw_height(trees, M)
print(f"{max_height}")