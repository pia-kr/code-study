# 핵심 개념 : N 을 나누는 최수의 수는 N-1 최수의 수 + 1 / 2로 나누기 / 3으로 나누기 경우 중 최소

N = int(input())

ans = [0]* (N+1)
# 1은 아무것도 안해도 되기에 0, 0은 고려 X
for i in range(2,N+1):
    ans[i] = ans[i-1] + 1

    if i % 2 == 0:
        ans[i] = min(ans[i], ans[i//2] + 1)
    if i % 3 == 0:
        ans[i] = min(ans[i], ans[i//3] + 1)
print(ans[N])