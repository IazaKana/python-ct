a = int(input())
b = list(input())
sum = 0

for i in b:
    sum = sum + int(i)

print(sum)

# new
# 입력 받은 것은 배열로 한번에 선언 가능
# for문의 i부분은 int타입이 아닌 str타입
# 파이썬에서는 배열과 리스트를 구분하지 않음
