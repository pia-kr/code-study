# 문제 : 시간초과 뜸 -> 빠른 입출력 써보기
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
highs = list(map(int, input().split()))

left_count = [0] * N
left_num = [0] * N

# 스택 이용
stack = []
for i in range(N):
    while stack and stack[-1][0] <= highs[i]:
        stack.pop()
    left_count[i] = len(stack)
    if stack:
        left_num[i] = stack[-1][1]
    else:
        left_num[i] = -1
    stack.append((highs[i], i))

right_count = [0] * N
right_num = [0] * N

stack = []
for i in range(N-1, -1, -1):
    while stack and stack[-1][0] <= highs[i]:
        stack.pop()
    right_count[i] = len(stack)
    if stack:
        right_num[i] = stack[-1][1]
    else:
        right_num[i] = -1
    stack.append((highs[i], i))

for i in range(N):
    total = left_count[i] + right_count[i]
    if total == 0:
        print(0)
    else:
        candidates = []
        if left_num[i] != -1:
            candidates.append(left_num[i])
        if right_num[i] != -1:
            candidates.append(right_num[i])

        nearest = min(candidates, key=lambda x: (abs(x - i), x))
        print(total, nearest + 1)