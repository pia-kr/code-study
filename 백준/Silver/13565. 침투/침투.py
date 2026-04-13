# 수정 : 런타임 에러로 인해 sys 이용하기
import sys
sys.setrecursionlimit(10**6)

yy = [-1, 0, 1, 0]
xx = [0, 1, 0, -1]

A = [[0] * 1001 for _ in range(1001)]
V = [[0] * 1001 for _ in range(1001)]
# 함수 정의
def dfs(y, x):
    V[y][x] = 1
    for i in range(4):
        Y, X = y + yy[i], x + xx[i]
        if Y < 1 or Y > M or X < 1 or X > N:
            continue
        if A[Y][X] or V[Y][X]:
            continue
        dfs(Y, X)
# 입력 받기
M, N = map(int, input().split())

for i in range(1, M + 1):
    # split X , strip
    row = input().strip()
    for j in range(1, N + 1):
        A[i][j] = int(row[j - 1])
# 탐색 하기
for i in range(1, N + 1):
    if not A[1][i] and not V[1][i]:
        dfs(1, i)
# 결과
print("YES" if 1 in V[M][1:N+1] else "NO")
