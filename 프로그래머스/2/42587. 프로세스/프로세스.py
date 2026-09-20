# deque import
from collections import deque

def solution(priorities, location):
    answer = 0
    
    # dq 생성 -> 값과 위치도 같이 저장하기
    dq = deque()
    for i in range(len(priorities)):
        # i 번째 값과 그 위치도 같이 저장
        dq.append((priorities[i], i))
        
    while dq:
        # 제일 앞쪽에서 부터 출력
        priority, index = dq.popleft()
        
        # 현재보다 높은 우선순위가 있는지 확인
        '''수정 : 
        for other_priority in dq:
            if any(priority < other_priority ):
         이렇게 하면 튜플 형태로 받기에 부등호 비교가 불가능
        '''
        if any(priority < other_priority for other_priority, _ in dq):
            dq.append((priority, index))
        else:
            answer += 1

            if index == location:
                return answer
    return answer





        