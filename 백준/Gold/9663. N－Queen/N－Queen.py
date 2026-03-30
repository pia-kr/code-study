# N-Queen 행, 대각선, 반대 대각선 확인
n = int(input())
cnt = 0

col_used = [False] * n
diag1_used = [False] * (2 * n)
diag2_used = [False] * (2 * n)

def dfs(row):
    global cnt

    if row == n:
        cnt += 1
        return

    for col in range(n):
        if col_used[col]:
            continue
        if diag1_used[row + col]:
            continue
        if diag2_used[row - col + n]:
            continue

        col_used[col] = True
        diag1_used[row + col] = True
        diag2_used[row - col + n] = True

        dfs(row + 1)

        col_used[col] = False
        diag1_used[row + col] = False
        diag2_used[row - col + n] = False

dfs(0)
print(cnt)