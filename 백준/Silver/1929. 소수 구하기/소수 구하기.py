# 생각: 입력 두 개 받음 -> 그 사이 반복을 돌림, 소수 구하는 함수 만들고 호출로 확인
# 소수 구하는 함수
import math

def prime(n):
    if n < 2:
        return False
    # 소수는 2부터 루트 n 까지의 수 중 나뉘어 지는게 있는지 확인해보면 됨
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m , n = map(int, input().split())

for i in range(m, n+1):
    if prime(i) == True:
        print(i)
    else:
        pass
