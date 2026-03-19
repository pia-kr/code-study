# A, B 원소의 개수 및 원소 입력받기 
# 생각 -> 집합이기에 set 이용하면 빠르게 가능 할 거 같음
# 생각2 -> 집합을 이용하니 sys  빠른 입력까지는 필요없지 않을까?
A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))


# A-B , B-A 차집합 구하기 
# 차집합 : difference 함수 이용
# 합집합 : | 이용

A_minus_B = A_set.difference(B_set)
B_minus_A = B_set.difference(A_set)

ans = A_minus_B | B_minus_A

print(len(ans))