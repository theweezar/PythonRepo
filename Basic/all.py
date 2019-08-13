# Cách khai báo và in ra màn hình - print bình thường và print format
name = "duc"
age = 20
array = ["duc","dong","dai",3,2,"ptit"]
# Dictionary trong python là 1 JSON, nó khác với javascript ở chỗ là từ khóa phải trong ""
dictionary = {
  "name":name,
  "age":age,
  "school":"PTIT"
}
# Tuple trong python nó cũng là 1 array, nhưng ko thể thay đổi giá trị của những phần tử
tup_le = ("Minh Duc",18,"Dai",13,"Dong",17)

print("Ho va ten : ",name);
print("Tuoi : ",age);
print(f"My name is {name} and I am {age} years old")
print("\nArray in python : ",array)
print("\nDictionary in python: ",dictionary)
print(f"Key 'name' in Dictionary: {dictionary['name']}")
print("\nTuple in Python: ",tup_le)

# Cách dùng if đối với array
if "duc" in array:
  print(f"\nThe word 'duc' is in this array: {array} ")

# Cách dùng if elif else
nAge = int(input("\nYour age : "))
if nAge < age:
  print(f"nAge: {nAge} < age: {age}")
elif nAge > age:
  print(f"nAge: {nAge} > age: {age}")
else:
  print(f"nAge: {nAge} = age: {age}")

# Loop
print("\nfor element in array:")
for element in array:
  print(element)
print("\nfor i in range(0,10): ")
for i in range(0,10):
  print(i)
print("\nk = 0; while k < 5: (do sth); k += 1")
k = 0
while k < 5:
  print(f"Still in loop k = {k}")
  k += 1

# Number process ( các phương thức để xử lý số)
import math # về cơ bản thì module math này khá giống bên javascript
number = 100
print(f"\nPow: {math.pow(number,2)}")
print(f"sqrt: {int(math.sqrt(number))}")
# ..... 

# String process ( các phương thức để xử lý chuỗi)
string = "Hoang Phan Minh Duc"
print(f"string.join('abc'): {string.join('abc')}")
print(f"string.split(' '): {string.split(' ')}")
# Replace 1 lần
print(f"string.replace('n','z',1): {string.replace('n','z',1)}")
# Replace tất cả chữ "n"
print(f"string.replace('n','z'): {string.replace('n','z')}")

# Cách pause màn hình bằng cách dùng input() nó giống getch() bên C
input()