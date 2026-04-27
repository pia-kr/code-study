## sqrt(n) 방식으로 시간초과 되어서 찾아본 세그먼트 트리 방법 - 나중에 다시 해보기
import sys

input = sys.stdin.readline
INF = 10**18

N = int(input())
arr = list(map(int, input().split()))
tree = [[0, 0] for _ in range(N << 1 | 1)]


## 두 노드 병합
def merge(L, R):
    ## 두 노드 간의 최소가 같다면
    if L[0] == R[0]:
        ## 더 작은 인덱스로 리턴하기
        return [L[0], min(L[1], R[1])]

    ## 아니라면 두 노드 중 최소가 더 작은 쪽 리턴
    if L[0] < R[0]:
        return L

    return R


## 바텀 업 세그트리
def update(i, v):
    tree[i + N - 1] = [v, i - 1]
    i += N - 1

    i >>= 1

    while i:
        tree[i] = merge(tree[i << 1], tree[i << 1 | 1])
        i >>= 1


def query(l, r):
    l += N - 1
    r += N - 1

    ret = [INF, INF]
    while l <= r:
        if l & 1:
            ret = merge(ret, tree[l])
            l += 1
        if ~r & 1:
            ret = merge(ret, tree[r])
            r -= 1
        l >>= 1
        r >>= 1

    ## 1 - index 로 변경
    return ret[1] + 1


## 초기화
for i in range(N):
    tree[i + N] = [arr[i], i]
for i in range(N - 1, 0, -1):
    tree[i] = merge(tree[i << 1], tree[i << 1 | 1])

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(query(b, c))