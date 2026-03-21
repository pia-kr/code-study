# 생각 : 두 수를 입력 받음 
# -> 그 수 중 큰 수를 기준으로 배수화 시키다가 작은 수로 나누어서 나머지가 0인 수 찾기
A, B = map(int, input().split())

# 둔 이유 : 반복문 돌릴때 경우 나누지 않기 위해서
if A < B :
    A, B = B, A
count = 1
ans = A
while(True):
    if ans % B == 0:
        break
    count += 1
    ans = A * count
print(ans)