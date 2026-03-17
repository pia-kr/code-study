#N, M 입력받기
N, M = map(int, input().split())
#N개의 수 입력받기
numbers = list(map(int, input().split()))
max_sum = 0
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i != j and i != k and j != k:
                sum = i + j + k
                if sum <= M and sum > max_sum:
                    max_sum = sum
print(max_sum)

