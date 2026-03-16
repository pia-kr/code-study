# 함수 선언
def f(n):
    # 초기
    if n == 1:
        return ["*"]
    a = f( n // 3)
    ans = []

    for i in a:
        ans.append( i * 3)
    for i in a:
        ans.append( i + " " * (n // 3) + i)
    for i in a:
        ans.append( i * 3)

    return ans
# N 입력받아서 출력하기
N = int(input())
print("\n".join(f(N)))