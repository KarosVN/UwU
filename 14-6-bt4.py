a = []
n = int(input("Nhập phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ",i + 1,":", end = ' ')
    x = int(input())
    a.append(x)
k = int(input('Nhập phần tử bạn muốn chia của dãy đầu tiên: '))
print('Dãy đầu:',a[:k])
print('Dãy sau:',a[k:])
