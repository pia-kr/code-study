# 생각 : 문자열 list로 입력 받음 
# -> 크기가 1~len(S) 크기까지 모든 경우의 수 생성
# set으로 만들면 중복 제거됨 -> 크기 출력

S = input()
ans_set = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        ans_set.add(S[i:j+1])
print(len(ans_set))