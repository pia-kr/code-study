# N, M 입력받기
N,M = map(int, input().split())
# 포켓몬 딕셔너리 생성 - 도감번호, 이름
pokemon = {}
for i in range(1,N+1):
    key = i
    value = input()
    pokemon[key] = value
reverse_pokemon = {v:k for k, v in pokemon.items()}
answer = []
# key -> value / value -> key
for j in range(M):
    ans = input()
    if ans.isdigit():
        answer.append(pokemon[int(ans)])
    else:
        
        answer.append(reverse_pokemon[ans])
for i in range(M):
    print(answer[i])

