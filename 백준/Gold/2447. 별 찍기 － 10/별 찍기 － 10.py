# 최종 정리 버전 - 배열 안에 배열로
def f(N):
    # 배열을 반환시키기
    if N == 1:
        return ["*"]
    # 9*9 배열이면 그 각 칸 안에는 3*3 일때의 f(n)이 들어가면 됨
    a = f(N//3)
    # 정답 배열 넣을 배열
    ans = []
    # 1, 2, 3번째
    for i in a:
        ans.append(i + i + i)
    # 4, 5, 6번째 -> * 5번째는 빈칸임
    for i in a:
        ans.append(i + " "*(N//3) + i)
    # 7, 8, 9번째 배열
    for i in a:
        ans.append(i + i + i)
    return ans

# N 입력받기
N = int(input())
# 배열을 연달아 출력해주는 join
print("\n".join(f(N)))