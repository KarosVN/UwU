a = int(input());
t = 1;
if (a > 0):
    for i in range(0, a):
        t *= i + 1;
    print('giai thua cua {0} la {1}'.format(a,t));
else:
    print('Moi nhap lai');
print();
