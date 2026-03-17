# N 입력받기
N = int(input())
# 최소개수를 구하는 것 이기에 5를 먼저 계산 후 3
count = -1
for i in range(N//5, -1, -1):
    if (N - 5*i) % 3 == 0:
        count = (i + (N - 5*i) // 3)
        break
    
print(count)

