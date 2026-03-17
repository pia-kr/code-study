x = input().upper()
count_x = []
del_x = list(set(x))
y = 0
for i in del_x:
    count_x.append(x.count(i))
    
if count_x.count(max(count_x)) > 1:
    print('?')
    
else :
    for i in range(len(del_x)):
        if max(count_x) == count_x[i]:
            y = i
            
    print(del_x[y])