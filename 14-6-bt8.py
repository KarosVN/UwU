a,b = [], []
n = int(input("Nhập phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ",i + 1,":", end = ' ')
    x = int(input())
    a.append(x)
for j in range(n - 1, 0, -1):
    for i in range (n - 2, -1, -1):
        if a[i] > a[j]:
            b.append((a[j],a[i]))
print(b)
