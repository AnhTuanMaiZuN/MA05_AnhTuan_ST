'''
#2.Tiền điện: Trong tháng, người dùng tiêu thụ x (kWh) điện. Nếu người dùng tiêu thụ:
Dưới 50 kWh: Đơn giá 1.728 đồng/kWh
Từ 51 đến 100 kWh: Đơn giá 1.768 đồng/kWh
Từ 101 đến 200 kWh: Đơn giá 2.074 đồng/kWh
Từ 201 đến 300 kWh: Đơn giá 2.612 đồng/kWh
Từ 301 đến 400 kWh: Đơn giá 2.919 đồng/kWh
Từ 401 trở lên: Đơn giá 3.015 đồng/kWh
Hãy xác định bài toán, vẽ sơ đồ khối và viết chương trình nhập vào số kWh điện mà người tiêu dùng tiêu thụ, tính và đưa ra màn hình số tiền điện phải trả. 
'''
x = int(input("Số kWh người dùng tiêu thụ trong tháng là: "))
if (x <= 50):
    print("Tiền điện phải trả là:", x * 1.728)
elif (x >= 51):
    print("Tiền điện cần phải trả là:", x * 1.768)
elif (x >= 101):
    print("Tiền điện cần phải trả là:", x * 2.074)
elif (x >= 201):
    print("Tiền điện cần phải trả là:", x * 2.612)
elif (x >= 301):
    print("Tiền điện cần phải trả là:", x * 2.919)
elif (x >= 401):
    print("Tiền điện cần phải trả là:", x * 3.015)