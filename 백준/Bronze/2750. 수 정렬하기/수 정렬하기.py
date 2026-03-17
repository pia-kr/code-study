# N 입력받기
N = int(input())
# N개의 정수 입력받기
numbers = []
for i in range(N):
    numbers.append(int(input()))
# 오름차순 정렬
numbers.sort()
for i in range(N):
    print(numbers[i])