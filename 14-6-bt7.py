a1, a2 = [], []
n1 = int(input("Nhập phần tử của list 1: "))
for i in range(n1):
    print("Nhập phần tử thứ",i + 1,"của list 1:", end = ' ')
    x = int(input())
    a1.append(x)
n2 = int(input("Nhập phần tử của list 2: "))
for i in range(n2):
    print("Nhập phần tử thứ",i + 1,"của list 2:", end = ' ')
    x = int(input())
    a2.append(x)
for i in range(n1):
    for j in range(n2):
        if a1[i] == a2[j]:
            print('2 list có phần tử chung')
            break
