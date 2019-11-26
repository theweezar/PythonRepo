import numpy as np

# Khởi tạo ma trận
# Ma trận 1x1
a = np.array([1,2,3,4])
# ma trận 2x3
b = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(b)

print(f"\nDimension of b: {b.ndim}")

print(f"\nb (Row = {b.shape[0]} and Column = {b.shape[1]})")

# Nó hoạt động khá giống mảng 2 chiều
print(f"\nb[1][2] = {b[1][2]}")

# lấy nguyên 1 cái hàng
print(f"\nFirst row of b = {b[0,:]}")

# lấy nguyên 1 cái cột
print(f"\nFirst column of b = {b[:,0]}")

# get phân tử nhỏ nhất trong ma trận
print(f"\nMin of matrix b : {np.min(b, axis = 1)}")

# get phần tử lớn nhất trong ma trận theo từng hàng - axis = 1 (row) - axis = 0 (column) có thể
# áp dụng luôn cho cả phương thức np.min()
print(f"\nMax of every row in b : {np.max(b, axis = 1)}")

# phương thức cộng tất cả phần tử bên trong ma trận
print(f"\nSum of matrix = {np.sum(b)}")

# phương thức cộng tất cả phần tử ở từng cột trong ma trận
print(f"\nSum of every column in matrix= {np.sum(b, axis = 0)}")

# phương thức biến hình - reshape(row,col)- nhưng phải đúng chuẩn
# và phải tính hàng, cột làm sao cho đủ phần tử, ko thì nó sẽ báo lỗi
c = b.reshape(4,2)
print(c)

# phương thức khởi tạo ma trận với mọi phần tử = 0, trong trường hợp này là ma trận 3x4
zeroMatrix = np.zeros((3,4))
print(zeroMatrix)

# phương thức khởi tạo ma trận với mọi phần tử bằng nhau
fullMatrix = np.full((3,4),5)
print(fullMatrix)

# phương thức nhân 2 ma trận lại với nhau, trong trường hợp này a x c 
# số cột của a phải bằng số hàng của c, nếu ko thì nó sẽ báo lỗi
abMul = np.matmul(a,c) 
print(f"\nabMul: {abMul}")

# phương thức vstack (push theo hàng) - tức là add thêm nhiều hàng, nhưng những hàng đó phải giống nhau
# về mặt cấu trúc

v1 = np.array([2,5,6,7])
v2 = np.array([5,2,6,8])

vAll = np.vstack((a,v1,v2))

print(f"\nvAll: {vAll}")

# phương thức hstack (push theo cột) - tức là add thêm nhiều cột, gộp nhiều ma trận lại vs nhau, nhưng
# những ma trận đó phải cùng cấu trúc luôn, thiếu hay dư là sẽ báo lỗi
p = np.array([[2,5,73,2],[75,22,5,7]])

hAll = np.hstack((b,p))

print(f"\nhAll: {hAll}")

input()
