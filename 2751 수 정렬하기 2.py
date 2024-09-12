import sys
import heapq

N = int(sys.stdin.readline()) 
NArray = []
a = []
b = []
for i in range(N):
    NArray.append(int(sys.stdin.readline()))

a = NArray[:N//2]

b = NArray[N//2:]
mergedList = list(sorted(a + b))
for i in range(len(mergedList)):
    print(mergedList[i])
