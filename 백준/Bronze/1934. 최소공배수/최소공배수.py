# 생각: 입력받음 -> 작은거 배수 시키다가 큰거로 나누어지면 끝
# 수정1 : 너무 오래걸림 -> 최대 공약수 찾아서 두 수를 곱한 후 그 수로 나누기
# 보통은 import math 후 gcd를 이용하지만 직접 구해보기
# 참고 : 유클리드 호제법

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
# T 입력받기
T = int(input())
ans = []
for i in range(T):
    A, B = map(int, input().split())
    ans.append((A * B) // gcd(A, B))
for i in ans:
    print(i)    

