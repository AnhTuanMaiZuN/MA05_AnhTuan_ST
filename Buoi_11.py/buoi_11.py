'''
def greeting(name):
    fullname = ""
    for i in name[1:len(name) - 1]:
        fullname += i + " "
    print("Xin chào", fullname)

fullname = input("Nhập họ và tên của bạn: ")
name = fullname.split(" ")
greeting(name)
'''
x = 100
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)