n = input("Hãy nhập vào một dãy số: ")
list = n
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)