def solution(s):
    # 스택 생성
    stack = []
    answer = True
    for i in s:
        # 앞에서 부터 읽으며 ( 인지 ) 인지 확인
        if i == '(' :
            # 스택에 추가
            stack.append(i)
        else :
            # 지금 ) 이고, 스택에 무언가 있으면 = ( 가 스택에 있음
            if stack :
                stack.pop()
            # 지금 ) 인데 스택에 아무것도 없음 => 짝이 안맞음
            else:
                answer = False
    # 만약 반복을 다 하고 끝이 ( 로 끝나서 스택에 무언가 남은 경우
    if stack:
        answer = False
    
    return answer


