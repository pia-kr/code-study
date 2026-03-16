# 반복할 함수 만들기
def f(n):
    if n == 1:
        return "-"
    else:
        a = f(n // 3)
        b = " " * (n // 3)
        return a + b + a
# 계속 반복문 / 수정: 파일의 반복 끝 -> try/except으로
while True:
    try:
        # 입력받기
        N = int(input())
        ans = f(3 ** N)
        print(ans)
    except:
        break