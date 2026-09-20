from collections import deque

def solution(prices):
    answer = []
    # 가격을 deque 에 저장
    dq = deque(prices)
    while dq:
        current = dq.popleft()
        time = 0

        for next_price in dq:
            time += 1
            # 현재값 보다 다음 값이 더 작으면 = 가격이 떨어지는 경우가 생기면
            if current > next_price: 
                break

        answer.append(time)
    
    return answer