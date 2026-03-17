# 사람의 수 N 받기
N = int(input())

# N개의 줄에 걸쳐 2개의 런 5개의 트릭 점수 , 총 7개의 정수 받기
# 1등의 점수 저장 변수
max_score = 0
for i in range(N):
    ''' run1, run2, trick1, trick2, trick3, trick4, trick5 = map(int, input().split())
이렇게 하면 기니까 리스트로 받아서 0~1, 2~6 비교'''
    
    scores = list(map(int, input().split()))
    run_score = []
    trick_score = []
    sum = 0

    for i in range(2):
        run_score.append(scores[i])
    sum += max(run_score)
    for i in range(2, 7):
        trick_score.append(scores[i])
    sum += max(trick_score)

    # 최고값을 제거하였기에 그 다음값이 최고값
    trick_score.remove(max(trick_score))
    sum += max(trick_score)

    # 비교
    if sum > max_score:
        max_score = sum
print(max_score)