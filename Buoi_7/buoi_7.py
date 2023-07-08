'''
n = int(input("Nhập N:"))
while True:
    if(-1 < n < 100):
        print(n)
        if n == 99:
            break
        n += 1
    else:
        n = int(input("Nhập lại N:"))
print (100)
'''
n = int(input())
tong = n
while (n != 0):
    n = int(input())
    tong += n
if tong % 100 == 0:
    print("DEP")
elif tong % 100 == 55:
    print("TRUNG BINH")
else:
    print("XAU")