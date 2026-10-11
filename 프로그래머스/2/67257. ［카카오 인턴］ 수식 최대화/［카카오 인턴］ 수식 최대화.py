def solution(expression):
    answer = 0
    
    # expression을 우선 숫자와 연산자로 해서 쪼개서 정리하기
    e = []
    num = ""
    
    for i in expression:
        # 문자열이라면
        if i.isdigit():
            num += i
        # 연산자라면 => 이 앞까지 num에 숫자들 정리, 지금 i 는 연산자 
        else:
            e.append(int(num))
            e.append(i)
            num = ""
    # 마지막 i 는 숫자일텐데 else에 들어갈 연산자가 없으니 추가로 넣어주기
    e.append(int(num))
    
    # 가능한 6개의 경우 정리
    values = [
        ("+", "-", "*"),
        ("+", "*", "-"),
        ("-", "*", "+"),
        ("-", "+", "*"),
        ("*", "+", "-"),
        ("*", "-", "+"),
    ]
    
    for v in values:
        # 진짜를 수정하지 않고 복사본으로 시험
        test = e.copy()
        
        for i in v:
            while i in test:
                # 본인, 왼쪽, 오른쪽 값의 위치
                idx = test.index(i)
                left = test[idx - 1]
                right = test[idx + 1]
                # i 번째가 연산자라면 -> 숫자 연산자 숫자 일 것임
                if i == "+":
                    result = left + right
                elif i == "-":
                    result = left - right
                else:
                    result = left * right     
                # 숫자, 연산자, 숫자 세 항목을 결과 하나로 교체
                test[idx - 1:idx + 2] = [result]
                
        # 가능한 경우 중 가장 큰 값
        answer = max(answer, abs(test[0]))
    
    
    return answer


