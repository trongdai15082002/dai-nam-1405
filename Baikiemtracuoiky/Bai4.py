nameid = input ( "Nhập tên và id chuỗi:" )
id = []
id = re . sub ( r '\ D' , '' , nameid )
l = lại . findall ( r '\ d' , id )
t = tuple ( l )
print ( "Mã sinh viên là:" , id )
in ( l )
in ( t )