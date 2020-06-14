a = []
n = int(input("Nhập phần tử: "))
for i in range(n):
    print(f"Nhập phần tử thứ",i + 1,":", end = ' ')
    x = int(input())
    a.append(x)
p = input("Nhập nội dung muốn thêm vào: ")
a.append(p)
print(a)
