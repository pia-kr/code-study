n = int(input())

'''n이 1,000,000이니 생성자는 최대가 999,999 이기에 이 경우
생성자 + 54 = n, 생성자 = n-54, 생성자의 최솟값은 n-54'''
answer = 0

for M in range(max(0, n - 54), n):
    decomposition = M + sum(map(int, str(M)))
    if decomposition == n:
        answer = M
        break

print(answer)
