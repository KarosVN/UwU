s1 = input()
s2 = s1[0]
for i in range(1,len(s1)):
    if (s1[i] == s1[0]):
        s2 += '$'
    else: 
        s2 +=s1[i]
print(s2)
