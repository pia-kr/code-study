# 빠른 입출력 용 sys
import sys

N = int(sys.stdin.readline())

N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

#정답 배열 만들고 값이 있으면 그 곳에 1씩 추가하기
ans = [0]*M

# 수정 -> 배열 형 출력을 딕셔너리를 이용한 출력으로 바꾸기
dic = {}

for n in N_list:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

for m in M_list:
    if m in dic:
        print(dic[m], end=" ")
    else:
        print(0, end=" ")