import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for _ in range(N)]

# 길이 1
for i in range(N):
    dp[i][i] = 1

# 길이 2
for i in range(N - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1

# 길이 3 이상
for length in range(3, N + 1):   # 구간 길이
    for start in range(N - length + 1):
        end = start + length - 1
        if numbers[start] == numbers[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])