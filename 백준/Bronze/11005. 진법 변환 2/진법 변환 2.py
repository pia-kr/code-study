N, B = map(int, input().split())
answer = []

while N > 0 :
    if N%B < 10 :
        answer.append(str(N%B))
    else :
        answer.append(chr(N%B - 10 + ord('A')))
    N //= B
    
print(''.join(reversed(answer)))