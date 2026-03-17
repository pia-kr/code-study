# 변수들 입력받기
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
# 함수 정의하기
def f(n) :
    return a1*n + a0
def g(n):
    return n
# f <= c*g 범위 만족하는지 확인
ans = 1

for i in range(n0,101):
    if f(i) > c * g(i):
        ans = 0
        break

print(ans)