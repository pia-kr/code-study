# 생각 : N -> 정수 입력 받음
# sort로 오름차순
# 차이 구해서 가작 작은거 기준으로 빈 값 -> 리스트 이용할듯
from math import gcd
N = int(input())
tree = []
for i in range(N):
    tree.append(int(input()))

tree = sorted(tree)

# 차 가 몇 인지 보기
tree_minus = []
for i in range(N-1):
    tree_minus.append(tree[i+1] - tree[i])
'''
# 최종적으로 만들어야 하는 간격
total_minus = min(tree_minus)

# 수정 1: 배열보다 set으로 하는게 탐색시간이 훨씬 짧아짐
tree_set = set(tree)
start = tree[0]
end = tree[N-1]
count = 0
while(start < end):
    if (start + total_minus) in tree_set:
        start += total_minus
        pass
    else:
        count += 1
        start += total_minus
print(count)'''

# 수정2: 최소 간격을 간격들 간의 최소 공배수로 하면 됨

g = tree_minus[0]
for i in range(1, len(tree_minus)):
    g = gcd(g, tree_minus[i])

count = 0
for i in tree_minus:
    count += (i // g) -1
print(count)