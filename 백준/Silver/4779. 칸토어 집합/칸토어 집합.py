# 최종 수정본
def f(N):
    # 0을 고려 안하는 이유 : 3^N으로 받기에 최솟값이 1
    if N == 1:
        return '-'
    # 수정 : 변수 할당 굳이 하지말고 바로 하기
    else :
        return f(N//3) +' '*(N//3) + f(N//3)        

while(True):
    try:
        # 입력받기
        N = int(input())
        # N이 1이면 길이가 3짜리를 - - 모양으로 해야하기에 3의 N 제곱
        print(f(3**N))
    except:
        break