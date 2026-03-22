# 생각 : 분모를 최소 공배수 찾음
# 그 최소 공배수를 받기 위해 필요한 만큼 count를 하던 나누기를 하던 곱해야 하는 수 구함
# 분자에 그 값끼리 곱해서 더한게 합의 분자, 최소공배수가 분모
# 분자와 분모가 약분이 되는 수가 있는지 확인
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())


''' 수정2 : 이것도 구해지나 더 빠르게 하는 법 -> (a*b) // gcd(a,b) 하면 바로 최소공배수 구해짐 
# 최소 공배수 구하기
# 계산 빠르게 하기 위해 b1 < b2
b1, b2 = B1, B2
if B1 > B2:
    b1, b2 = B2, B1
s = 0
count = 1
while(True):
    count += 1
    s = b2 * count
    if s % b1 == 0:
        break
'''

s = (B1 * B2) // gcd(B1, B2)
# 중간 정리 s -> 분모의 최소 공배수 인 상태
# 분자
molecule = (s // B1) * A1 + (s // B2) * A2
# 분모
denominator = s

# 분자와 분모의 공약수 gcd이용해서 구하고 이후에 그 수로 나누기(1 이어도 나누어지니 그냥 전부 고려)


''' 수정1 : 이렇게 하면 두번째 gcd 호출시엔 바뀐 molecule 값으로 되버림 -> 중간에 저장 후 쓰기
molecule //= gcd(molecule, denominator)
denominator //= gcd(molecule, denominator)
'''
g = gcd(molecule, denominator)
molecule //= g
denominator //= g
print(molecule, denominator)