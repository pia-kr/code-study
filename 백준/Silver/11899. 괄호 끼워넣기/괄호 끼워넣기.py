# 입력 받은 것 중 닫는 괄호 기준으로 스택에서 제거 + 모자란 횟수 구하기
# 입력 받기
s = list(input())
stack = []
brackets = ["(", ")"]
count = 0
for i in s:
    if i in brackets:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                count += 1
# 수정 : 스택에 열린 괄호만 남은 경우도 추가해 줘야 함
print(count + len(stack))