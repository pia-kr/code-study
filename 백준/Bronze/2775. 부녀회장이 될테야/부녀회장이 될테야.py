# test case 입력받기 -> 개수 모르니 리스트에 입력받기

def f(k,n):
    ans = [[0] * (n+1) for _ in range(k+1)]

    # 첫 줄이 있으니 배열 반복 범위 잘 조절하기
    for i in range(0, k+1):
        for j in range(1, n+1):
            if i == 0:
                ans[i][j] = j
            else:
                ans[i][j] = ans[i][j-1] + ans[i-1][j]
    return ans[k][n]
N = int(input())
ans_list = []
for i in range(N):
    k = int(input())
    n = int(input())
    ans_list.append(f(k,n))
for i in range(N):
    print(ans_list[i])