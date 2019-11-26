import numpy as np

# Khởi tạo ma trận
# Ma trận 1x1
a = np.array([1,2,3])
# ma trận 2x3
b = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(b)

print(f"Dimension of b: {b.ndim}")

print(f"b (Row = {b.shape[0]} and Column = {b.shape[1]})")

# Nó hoạt động khá giống mảng 2 chiều
print(f"b[1][2] = {b[1][2]}")

# lấy nguyên 1 cái hàng
print(f"First row of b = {b[0,:]}")

# lấy nguyên 1 cái cột
print(f"First column of b = {b[:,0]}")

# get phân tử nhỏ nhất trong ma trận
print(f"Min of matrix b : {np.min(b, axis = 1)}")

# get phần tử lớn nhất trong ma trận theo từng hàng - axis = 1 (row) - axis = 0 (column) có thể
# áp dụng luôn cho cả phương thức np.min()
print(f"Max of every row in b : {np.max(b, axis = 1)}")

# phương thức cộng tất cả phần tử bên trong ma trận
print(f"Sum of matrix = {np.sum(b)}")

# phương thức cộng tất cả phần tử ở từng cột trong ma trận
print(f"Sum of every column in matrix= {np.sum(b, axis = 0)}")

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
input()
