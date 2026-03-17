alphabet = input()
c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in c_alphabet:
    alphabet = alphabet.replace(i,"1")
print(len(alphabet))