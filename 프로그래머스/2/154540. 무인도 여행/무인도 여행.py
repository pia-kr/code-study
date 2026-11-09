def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    
    # 이동용
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    #dfs 정의
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        total = 0

        while stack:
            x, y = stack.pop()
            total += int(maps[x][y])

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

        return total

    result = []

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(dfs(i, j))

    if not result:
        return [-1]

    return sorted(result)