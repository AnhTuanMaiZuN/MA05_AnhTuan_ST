'''
n = int(input("Nhập n: "))
# Để kiểm tra n là số chẵn thì n phải chia hết cho 2
# Khi nào n chia hết cho 2
# khi số dư = 0

if (n % 2 == 0):
    print(n, "là số chẵn")
else:
    print(n, "là số lẻ")
'''
'''
print("1. Là quả táo")
print("2. Là quả cam")
print("3. Là quả xoài")
print("4. Là các quả còn lại")

qua = int(input("Nhập quả cần bỏ vào giỏ: "))
if (qua == 1):
    print("Bỏ vào giỏ A")
elif (qua == 2):
    print("Bỏ vào giỏ B")
elif (qua == 3):
    print("Bỏ vào giỏ C")
else:
    print("Bỏ vào giỏ D")
'''
n = float(input("Nhập n: "))

if (n > 0):
    print("Trị tuyệt đối của:", n, "là:", n)
else:
    n - n * (-1)
    print("Trị tuyệt đối của", n, "là:", n * (-1))