A, B, V = map(int, input().split())

last_h = V - A

day = (last_h + (A-B) -1 ) // (A-B) + 1

print(day)