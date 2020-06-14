a, b, j = [], [], 0
n = int(input("Nhập phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ",i + 1,":", end = ' ')
    x = int(input())
    a.append(x)
a.sort()
i = 0
while (i < n):
    b.append(a.count(a[i]))
    i += b[j]
    j += 1
for i in range(n):
    if a.count(a[i]) == max(b):
        print("Phần tử xuất hiện nhiều nhất là {0} với {1} lần xuất hiện".format(a[i],max(b)))
        break
