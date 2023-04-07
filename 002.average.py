a = int(input())
b = list(map(int, input().split()))
max_score = max(b)
c = 0

for i in range(a):
    c = c + (b[i] / max_score * 100)

print(c/a)

# 정답
# n = input()
# mylist = list(map(int, input().slkut()))
# mymax = max(mylist)
# sum = sum(mylist)
# print(sum * 100 / mymax / int(n))

# new
# map을 사용해서 정수로 변환 - map(int, input().split())
# sum 함수 존재
# 구간 합 - S[i] = S[i-1] + A[i]
