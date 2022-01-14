import re
str = ', '
infor = input("Nhập vào chuỗi tên và mã sinh viên: ")
value = str.join(infor)
list=value.split(",")
tuple=tuple(list)
print ("Danh sách là: ",list, end=" ")
print("")
print ("Tuple là: ",list, end=" ")