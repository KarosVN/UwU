a, b = [], []
n = int(input("Nhập phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ",i + 1,":", end = ' ')
    x = int(input())
    a.append(x)
b.append(a[0])
for i in range(1,n):
    t = 0
    for j in range(i):
        if a[i] != a[j]:
            t += 1
        if t == i:
            b.append(a[i])
print(len(b))
