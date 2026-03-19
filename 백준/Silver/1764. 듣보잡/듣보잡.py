# 생각 : 듣도못함 -> 리스트, 보도못함 -> 입력받으면서 리스에 넣지 말고 중첩인 애면 출력하고 아니면 패스

# N M 입력받기 *수정: 빠른 입력 이용하기

import sys
N, M = map(int, sys.stdin.readline().split())
'''수정3: 리스트와 리스트를 겹치는거 비교만 하는 용도로 리스트를 쓰기엔
    너무 수행시간이 길어짐 -> 단순 비교용이면 set 이용하기
N_list = []
ans = []
for i in range(N):
    # 수정2 : readline 쓸때는 내 enter 키 까지 같이 입력받음 -> strip()으로 개행을 제거해주기
    N_list.append(sys.stdin.readline().strip())
for j in range(M):
    M_list = sys.stdin.readline().strip()
    
    if M_list in N_list:
        ans.append(M_list)
ans = sorted(ans, reverse = False)
print("\n".join(ans))'''
# 최종 정리본

N_set = set()
for i in range(N):
    N_set.add(sys.stdin.readline().strip())
M_set = set()
for i in range(M):
    M_set.add(sys.stdin.readline().strip())
# set을 이용할 때는 & 연산자로 바로 겹치는 부분을 출력할 수 있음
ans = sorted(N_set & M_set)
print(len(ans))     
print("\n".join(ans))
