# 두 문자열 리스트로 입력받기
first = list(input().strip())
second = list(input().strip())

ans = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

# DP로 LCS 길이 구하기
for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i - 1] == second[j - 1]:
            ans[i][j] = ans[i - 1][j - 1] + 1
        else:
            ans[i][j] = max(ans[i][j - 1], ans[i - 1][j])

num = ans[len(first)][len(second)]
print(num)

# 역추적으로 LCS 문자열 구하기
if num != 0:
    i = len(first)
    j = len(second)
    result = []

    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            result.append(first[i - 1])
            i -= 1
            j -= 1
        else:
            if ans[i - 1][j] >= ans[i][j - 1]:
                i -= 1
            else:
                j -= 1

    result.reverse()
    print(''.join(result))