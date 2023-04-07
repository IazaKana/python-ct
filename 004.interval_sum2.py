import sys
input = sys.stdin.readline
n, m = map(int, inpu().split())
A = [[0] * (n+1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 파이썬에서는 반복을 수행하되 변수 값이 필요 없을 때 언더바(_)를 사용함.