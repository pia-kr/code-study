# 이중배열에 각각 0번을 할당하고 겹치면 1만들고 이후에 비교

# 두 문자열 리스트로 입력받기
first = list(input())
second = list(input())

# [first][second]
# + 1 하는 이유: 첫 줄에 0으로 찬 배열이 필요하기에, 나머지만 채울 예정

ans = [[0] * (len(second)+1) for _ in range(len(first)+1)]

# 첫 줄이 있으니 배열 반복 범위 잘 조절하기
for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        # first[i] == 0 and second[i] == 0 이 문장은 top - down으로 재귀 호출 시 필요
        # bottom up 방식에는 필요없음
        # first second에서 1 1 번지가 ans에서는 2 2 번지임!
        # first second에서는 index가 1씩 낮음
        if first[i-1] == second[j-1]:
            ans[i][j] = ans[i-1][j-1] + 1
        else:
            ans[i][j] = max(ans[i][j-1], ans[i-1][j])
        

print(ans[len(first)][len(second)])