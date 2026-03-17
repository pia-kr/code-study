# 3가지 기술 난이도 입력받기
one_hand , no_look, phone = map(int, input().split())
# 참여한 동아리의 수 입력받기
n = int(input())
# 가장 큰 동아리의 점수 합을 받을 변수
max_sum = 0
j = 0
# 동아리의 횟수만큼 반복
while(j<n):
    sum = 0
    for i in range(3):
        # 동아리 내의 총 점을 입력받아 계산
        a,b,c = map(int, input().split())    
        sum += a*one_hand + b*no_look + c*phone
    if sum > max_sum:
        max_sum = sum
    j += 1
print(max_sum)