x = list(input())
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = [-1]*26
for i in range(26):
    for j in range(len(x)):    
        if a[i] == x[j]:
            b[i] = j
            break     
for i in range(26):
    print(b[i],end =' ')