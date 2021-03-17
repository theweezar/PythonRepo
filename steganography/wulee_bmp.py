import matplotlib.image as image

# image_file = open('input_image.bmp','rb')
# # Lượt con trỏ xuống cuối file để biết được size của file ảnh
# image_file.seek(-1, 2)
# # Tổng byte của file - 54 bytes header đi sẽ ra những byte còn lại của điểm ảnh
# image_size = image_file.tell() - 54
# # Lượt con trỏ lên đầu file
# image_file.seek(0,0)

# image_bytes = []
# r = []
# g = []
# b = []

# for i in range(0, int(image_size / 3)):
#   r.append(ord(image_file.read(1)))
#   g.append(ord(image_file.read(1)))
#   b.append(ord(image_file.read(1)))

# print('len(r):',len(r))
# print('len(g):',len(g))
# print('len(b):',len(b))

bmp_image = image.imread('input_image.bmp')
print('bmp_image.shape:',bmp_image.shape)
print(bmp_image[:,:,0])