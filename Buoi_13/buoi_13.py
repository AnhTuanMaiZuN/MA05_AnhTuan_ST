'''
def Nhap():
    return int(input("Nhập cạnh căn phòng = "))

def Tinh_dien_tich(canh):
    return canh * canh

def Tinh_so_gach(dientich):
    return dientich // 400

def Xuat(kq, kq1):
    print("Diện tích căn phòng là = {}". format(kq))
    print("Số viên gạch = {}". format(kq1))

canh = Nhap()
kq = Tinh_dien_tich(canh)
kq1 = Tinh_so_gach(kq)
Xuat(kq, kq1)
'''
def Nhap():
    print("Điểm của An là: ")
    return[float(x)for x in input().split()]

def DTB(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

def GT2(list):
    list.sort(reverse = True)
    n_max = list[0]
    for i in list():
        if i < n_max:
            return i
    return -1

def Xuat(dtb, gt_l2):
    print("Điểm trung bình của An là: ", dtb)
    if (gt_l2 == -1):
        print("Không có giá trị lớn thứ 2")
    else:
        print ("Điểm số lớn thứ hai của An là:", gt_l2)

list = Nhap()
dtb = DTB(list)
Xuat(dtb, list[-1])
gt_l2 = GT2(list)