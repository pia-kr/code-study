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
        # 이 열에 퀸이 있는지
        if col_used[col]:
            continue
        # 이 대각선에 퀸이 있는지
        if diag1_used[row + col]:
            continue
        # 반대 대각선에 퀸이 있는지
        if diag2_used[row - col + n]:
            continue

        col_used[col] = True
        diag1_used[row + col] = True
        diag2_used[row - col + n] = True
        # 다음 행에서 실행해봄
        dfs(row + 1)
        # 마지막 행 까지 다 했으면 -> 퀸을 놓은 자리를 다시 비워줌
        col_used[col] = False
        diag1_used[row + col] = False
        diag2_used[row - col + n] = False

dfs(0)
print(cnt)