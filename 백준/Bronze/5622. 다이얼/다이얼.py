x = list(input())
num = 0
case_2 = ['A', 'B', 'C']
case_3 = ['D', 'E', 'F']
case_4 = ['G', 'H', 'I']
case_5 = ['J', 'K', 'L']
case_6 = ['M', 'N', 'O']
case_7 = ['P', 'Q', 'R', 'S']
case_8 = ['T', 'U', 'V']
case_9 = ['W', 'X', 'Y', 'Z']
for i in range(len(x)):
    if x[i] in case_2 :
        x[i] = 2
    elif x[i] in case_3 :
        x[i] = 3
    elif x[i] in case_4 :
        x[i] = 4
    elif x[i] in case_5 :
        x[i] = 5
    elif x[i] in case_6 :
        x[i] = 6
    elif x[i] in case_7 :
        x[i] = 7
    elif x[i] in case_8 :
        x[i] = 8
    else :
        x[i] = 9
        
for i in range(len(x)):
    num = num + int(x[i]) + 1
    
print(num)