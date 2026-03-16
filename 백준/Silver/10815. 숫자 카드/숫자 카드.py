# 수정사항 : 빠른 입력을 위한 sys 이용 수정3: 리스트도 빠른 입력
import sys
N = int(sys.stdin.readline())
N_list = list(map(int , sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int , sys.stdin.readline().split()))

# 수정2 : 출력을 배열 만들고 출력말고 바로 출력
# 수정4 : 배열 출력말고 딕셔너리를 출력하면 더 빠름
dict_ans = {}
for i in range(len(N_list)):
    dict_ans[N_list[i]] = 0

for j in range(M):
    if M_list[j] in dict_ans:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
