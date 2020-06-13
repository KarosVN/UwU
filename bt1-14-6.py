a, tong, tich = [], 0, 1
n = int(input("Nhập phần tử: "))
for i in range(n):
    x = int(input())
    a.append(x)
for i in range(n):
    tong += a[i]
    tich *= a[i]
print("tong = ", tong)
print("tich = ", tich)
