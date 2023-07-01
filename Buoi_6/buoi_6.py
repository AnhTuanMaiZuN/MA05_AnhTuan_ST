'''
a = int(input("Nhập số nguyên a = "))
b = int(input("Nhập số nguyên b = "))
sum = 0
if (a % 2 == 1):
    a += 1
for i in range(a,b,2):
        sum += i
        # sum = sum + 1
print(f"Tổng các số chẵn của {a} đến {b} là:", sum)
'''
'''
a = int(input("Nhập a ="))
b = int(input("Nhập b ="))
if (a < 1 or a > 10):
    print("Khoảng a,b ko hợp lệ trong cửu chương.")
else:
    for i in range(a,b+1):
        print(f"Bảng cửu chương {i} là:")
        for j in range (1,10):
            print(f"{i} * {j} = {i} = {i*j}")
'''
'''
n = int(input("Nhập số nguyên n:"))
a = 1
sum = 0
if (a % 2 == 1):
    a += 1
for i in range(a,n,2):
    sum += i
    # sum = sum + 1
print(f"Tổng các số chẵn của 1 đến {n} là:", sum)
'''
n = int(input("Nhập số nguyên n:"))
for i in range(n):
    for j in range(n):
         print(end ="")
    for j in range(i+1):
        print("*", end="")
    print()