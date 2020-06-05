a = int(input());
b = int(input());
if (b < a):
    for i in range(b + 1, a):
        print(i, end = ' ');
else: 
    for i in range(a + 1,b):
        print(i, end = ' ');
print();
