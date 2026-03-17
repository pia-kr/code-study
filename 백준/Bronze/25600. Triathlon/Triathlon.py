# 참가자 수 받기
N = int(input())
# 참가자들의 점수 받기
# 1등의 점수 저장용 변수
score_max = 0
for i in range(N):
    a,d,g = map(int, input().split())
    score = a*(d+g)
    if(a == (d+g)):
        score = score*2

    # 1등의 점수보다 높은 점수가 들어오면 1등의 점수 갱신
    if score > score_max:
        score_max = score
print(score_max)