# import thư viện và dữ liệu vào Python
nhập  numpy  dưới dạng  np
nhập  matplotlib . pyplot  as  plt
nhập  hệ thống
print ( phiên bản sys . )
từ  hàng xóm nhập khẩu sklearn  , bộ dữ liệu

# Tải dữ liệu và hiển thị một số mẫu dữ liệu. Các class được gán nhãn là 0, 1 và 2.
iris  =  bộ dữ liệu . load_iris ()
iris_X  =  mống mắt . dữ liệu
iris_y  =  mống mắt . Mục tiêu
print ( "Số lớp:% ​​d"  % len ( np . unique ( iris_y )))
print ( 'Số điểm dữ liệu:% d'  % len ( iris_y ))

X0  =  iris_X [ iris_y  ==  0 ,: ]
print ( ' \ n Các mẫu từ lớp 0: \ n ' , X0 [: 5 ,: ])

X1  =  iris_X [ iris_y  ==  1 ,: ]
print ( ' \ n Các mẫu từ lớp 1: \ n ' , X1 [: 5,: ])

X2  =  iris_X [ iris_y  ==  2 ,: ]
print ( " \ n Mẫu từ lớp 2: \ n " , X2 [: 5 ,: ])
từ  sklearn . model_selection  import  train_test_split
X_train , X_test , y_train , y_test  =  train_test_split (
     iris_X , iris_y , test_size = 50 )

# Tách tập và thử nghiệm
print ( "Kích thước đào tạo:% d"  % len ( y_train ))
print ( "Kích thước thử nghiệm:% d"  % len ( y_test ))
clf  =  hàng xóm . KNeighborsClassifier ( n_neighbors  =  1 , p  =  2 )
clf . phù hợp ( X_train , y_train )
y_pred  =  clf . dự đoán ( X_test )

# xét trường hợp đơn giản K = 1, tức là với mỗi điểm kiểm tra dữ liệu ta chỉ nhận ra 1
# điểm đào tạo dữ liệu gần nhất và lấy nhãn của điểm đó để dự đoán cho điểm kiểm tra này
print ( "In kết quả cho 20 điểm dữ liệu thử nghiệm đầu tiên:" )
print ( "Các nhãn được dự đoán:" , y_pred [ 20 : 40 ])
print ( "Sự thật cơ bản:" , y_test [ 20 : 40 ])
clf  =  hàng xóm . KNeighborsClassifier ( n_neighbors  =  10 , p  =  2 )
clf . phù hợp ( X_train , y_train )
y_pred  =  clf . dự đoán ( X_test )

# Phương pháp đánh giá
từ  sklearn . số liệu  nhập  chính xác_score
# Xem gần nhất 1 điểm
in ( "Độ chính xác của 1NN:% 2f %%"  % ( 100 * accuracy_score ( y_test , y_pred )))
# Gần nhất 10 điểm
clf  =  hàng xóm . KNeighborsClassifier ( n_neighbors  =  10 , p  =  2 )
clf . phù hợp ( X_train , y_train )
y_pred  =  clf . dự đoán ( X_test )
in ( "Độ chính xác của 10NN có quyền biểu quyết lớn:% 2f %%"  % ( 100 * accuracy_score ( y_test , y_pred )))