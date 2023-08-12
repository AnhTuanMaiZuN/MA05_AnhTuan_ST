'''
for i in range(10,50):
    if (i % 3 == 0):
        print(i)
'''
'''
sum = 1
gt = 1
for s in range(2,11):
    gt *= s
    sum += gt
print("tổng của s là:", sum)
'''
'''
for i in range(6,1000):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
        if sum > i:
            break
    if sum == i:
        print(i, end = " ")
'''
'''
x = int(input("Nhập x = "))
n = int(input("Nhập n = "))
n_gt = 1
gt = 1
sum = x
for i in range(2, n+1):
    gt *= i
    sum += pow(x,i)/gt
print(round(sum, 2))
'''