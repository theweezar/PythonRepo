import numpy as np 
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as image
from PIL import Image

# bmp_image = image.imread('input_image.bmp')
# print('bmp_image.shape:',bmp_image.shape)
# print(bmp_image[:,:,0])

# pyplot_image = plt.imread('input_image.bmp')
# print(pyplot_image)

class WuleeLastestVersion:
  def __init__(self):
    super().__init__()
    self.cover_image = None # ảnh gốc  
    self.key = None         # khóa 
    self.block_width = 0    # chiều rộng của 1 block
    self.block_height = 0   # chiều cao  của 1 block
    self.message = ""       # tin nhắn
    self.bin_message = ""
    self.hidden_count = 0   # số tin đã giấu 
    self.retrieve_message = "" # tin nhắn đã trích xuất
    self.retrieve_bin = ""
    self.retrieve_bin_temp = ""
    self.retrieve_count = 0    # số tin nhắn đã trích xuất
    self.retrieve_max = -1      # số tin trích xuất tối đa
    self.retrieve_done = False
    self.CHANNEL_BLUE = 0      
    self.CHANNEL_GREEN = 1
    self.CHANNEL_RED = 2

  def compare_test(self):
    print('Ma trận khóa:\n', self.key)
    print('Raw message :',self.message)
    print('Bin message :',self.bin_message)
    print('Bin retrieve:',self.retrieve_bin)
    print('Retrieve msg:',self.retrieve_message)

  def set_key(self, key_string):
    key = []
    # ord(c) chuyển kí tự thành ASCII và format theo binary độ dài 8 bit 
    # cho từng kí tự trong chuỗi
    bin_array = ['{0:08b}'.format(ord(c)) for c in key_string]
      # bin_array => [ '00101010', '01001001' , ... ] 
    
    # Duyệt từng chuỗi nhị phân 8 bit trong mảng trên  
    for bin_str in bin_array:
      # Chuyển từng kí tự trong chuỗi nhị phân 8 bit thành số nguyên 1 và 0 
      bin_matrix = [int(b) for b in bin_str]
        # bin_matrix => '00101010' => [0,0,1,0,1,0,1,0]

      # Sau đó, tiếp tục thêm vào mảng khóa
      key.append(bin_matrix)
        # key => [[0,0,1,0,1,0,1,0],..]
      
    # Chuyển mảng nhị phân 2 chiều thành ma trận 2 chiều
    self.key = np.array(key)
    # Lưu lại kích thước khối 
    self.block_height = self.key.shape[0]
    self.block_width = self.key.shape[1]
    # print('Word: \''+ key_string +'\' turn into:')
    # print(self.key)
    print('Sum key:',self.key.sum())
    
  def set_key_to_null(self):
    self.key = None
  
  # Các thao tác với biến -------------------------------
  def set_message(self, message):
    self.message = f"{len(message)}:{message}"
    for c in self.message:
      self.bin_message += '{0:08b}'.format(ord(c))

  def set_cover_image(self, path):
    self.cover_image = cv2.imread(path)
    # self.cover_image = np.array(Image.open(path))
    # self.cover_image.flags.writeable = True
    # print(dir(self.cover_image))

  def save_stego_image(self, file_name):
    cv2.imwrite(file_name, self.cover_image)

  # def set_retrieve_max(self, retrieve_max):
  #   self.retrieve_max = retrieve_max * 8

  def reset_when_hide_done(self):
    self.message = ""
    self.bin_message = ""
    self.hidden_count = 0

  def reset_when_retrieve_done(self):
    self.retrieve_count = 0
    self.retrieve_max = -1
    self.retrieve_message = ""
    self.retrieve_bin = ""
    self.retrieve_bin_temp = ""

  def get_cover_image_height(self):
    return self.cover_image.shape[0]

  def get_cover_image_width(self):
    return self.cover_image.shape[1]

  def get_total_pixels(self):
    return self.get_cover_image_height() * self.get_cover_image_width()
    
  def reset_when_hide(self):
    self.message = ""
    self.hidden_count = 0
    
  def reset_when_retrieve(self):
    self.retrieve_message = "" 
    self.retrieve_count = 0    
    self.retrieve_max = 0

  # Hàm xử lý chính --------------------------------------
  def calculate(self):
    return f"""Total number of pixels: {self.get_total_pixels()}
Key length maximum: {self.get_cover_image_height()}
Image height: {self.get_cover_image_height()}
Image width: {self.get_cover_image_width()}"""

  def fi_bin_random_replace(self, fi_bin, target, replace):
    for i in range(0, fi_bin.shape[0]):
      for j in range(0, fi_bin.shape[1]):
        if fi_bin[i, j] == target and self.key[i, j] == 1:
          # print('Before replace:\n',fi_bin,'====> sum:',fi_bin.sum())
          fi_bin[i, j] = replace
          # print('After replace:\n',fi_bin,'====> sum:',fi_bin.sum())
          return fi_bin
    return fi_bin

  def fi_bin_random_reverse(self, fi_bin):
    for i in range(0, fi_bin.shape[0]):
      for j in range(0, fi_bin.shape[1]):
        if self.key[i, j] == 1:
          if fi_bin[i, j] == 1:
            fi_bin[i, j] = 0
          else:
            fi_bin[i, j] = 1
          return fi_bin
    return fi_bin
  
  def fi_int_to_binary(self, fi):
    # logic y chang setkey
    fi_bin = []
    bin_array = ['{0:08b}'.format(int(c)) for c in fi]
    for bin_str in bin_array:
      bin_matrix = [int(b) for b in bin_str]
      fi_bin.append(bin_matrix)
    return np.array(fi_bin)

  def fi_binary_to_int(self, fi_bin):
    fi = [int(bin_str, 2) for bin_str in [''.join(str(b) for b in bin_arr) for bin_arr in fi_bin]]
    fi = np.array(fi)
    return fi
  
  def hide(self):
    print('Giấu tin---------------------------------')
    self.hide_in_channel(self.CHANNEL_BLUE)
    self.hide_in_channel(self.CHANNEL_GREEN)
    self.hide_in_channel(self.CHANNEL_RED)
  
  def hide_in_block_int(self, block_int, pos):
    # print(block_int)
    # exit(1)
    bin_char_to_hide = int(self.bin_message[self.hidden_count])
    # print(block_int)
    fi_bin = self.fi_int_to_binary(block_int)
    # print(fi_bin)
    # SUM ( fi ^ key )
    xor_sum = np.bitwise_xor(fi_bin, self.key).sum()
    # SUM ( key )
    key_sum = self.key.sum()
    if xor_sum > 0 and xor_sum < key_sum:
      if xor_sum % 2 == bin_char_to_hide:
        fi_bin = fi_bin
        # pass
      elif xor_sum == 1:
        # fi_bin = self.fi_bin_random_replace(fi_bin, 0, 1)
        fi_bin = self.fi_bin_random_replace(fi_bin, 1, 0)
      elif xor_sum == key_sum - 1:
        # fi_bin = self.fi_bin_random_replace(fi_bin, 1, 0)
        fi_bin = self.fi_bin_random_replace(fi_bin, 0, 1)
      else:
        fi_bin = self.fi_bin_random_reverse(fi_bin)
      new_xor_sum = np.bitwise_xor(fi_bin, self.key).sum()
      print('xor_sum:',xor_sum,'| Vị trí đúng:',pos,'| new_xor_sum:',new_xor_sum, '| Bit đang giấu:', bin_char_to_hide)
      self.hidden_count += 1
      block_int = self.fi_binary_to_int(fi_bin)
    else:
      print('xor_sum:',xor_sum,'| Vị trí ko đúng:',pos)

    return block_int
      

  def hide_in_channel(self, channel):
    # Trích xuất Channel
    img_channel = self.cover_image[:,:,channel]
    # Duyệt hết ảnh
    # Duyệt theo chiều cao ( height ) khóa
    for i in range(0, self.get_cover_image_height(), self.block_height) :  
      for j in range(0, self.get_cover_image_width()) :
        block_int = img_channel[i:i+self.block_height, j]
        # block_int = img_channel[i:i+self.block_height, j:j+1].reshape(1,-1)
        
        if self.hidden_count == len(self.bin_message):
          return
        
        # Đặt ra giới hạn cho những block có kích thước không đủ
        if block_int.shape[0] == self.block_height:
          block_int = self.hide_in_block_int(block_int, j)
          img_channel[i:i+self.block_height, j:j+1] = block_int.reshape(-1,1)

    # Gán ảnh channel vào ảnh gốc
    self.cover_image[:,:,channel] = img_channel
    
          

  def retrieve(self):
    print('Trích xuất---------------------------------')
    self.retrieve_in_channel(self.CHANNEL_BLUE)
    self.retrieve_in_channel(self.CHANNEL_GREEN)
    self.retrieve_in_channel(self.CHANNEL_RED)
    # self.bin_retrieve_to_string()
    self.retrieve_message = self.retrieve_message[1:]

  def retrieve_in_channel(self, channel):
    if self.retrieve_done is True:
      return
    # Trích xuất Channel
    img_channel = self.cover_image[:,:,channel]
    # Duyệt hết ảnh
    # Duyệt theo chiều cao ( height ) khóa
    for i in range(0, self.get_cover_image_height(), self.block_height) :
      if self.retrieve_count == self.retrieve_max:
        return
      for j in range(0, self.get_cover_image_width()) :
        block_int = img_channel[i:i+self.block_height, j]
        if self.retrieve_count == self.retrieve_max:
          return
        # Đặt ra giới hạn cho những block có kích thước không đủ
        if block_int.shape[0] == self.block_height:
          block_int = self.retrieve_in_block_int(block_int, j)
          
  def retrieve_in_block_int(self, block_int, pos):

    fi_bin = self.fi_int_to_binary(block_int)
    # SUM ( fi ^ key )
    xor_sum = np.bitwise_xor(fi_bin, self.key).sum()
    # SUM ( key )
    key_sum = self.key.sum()

    if xor_sum > 0 and xor_sum < key_sum:
      if xor_sum % 2 == 0:
        self.retrieve_bin_temp += "0"
      else:
        self.retrieve_bin_temp += "1"
      # self.retrieve_count += 1
      if len(self.retrieve_bin_temp) == 8:
        _ascii = int(self.retrieve_bin_temp, 2)
        if _ascii >= 32 and _ascii <= 126:
          if _ascii == 58 and self.retrieve_max == -1:
            self.retrieve_max = int(self.retrieve_message) + 1
            self.retrieve_message = ""
          if self.retrieve_max > 0:
            self.retrieve_count += 1
          self.retrieve_message += chr(_ascii)
          self.retrieve_bin += self.retrieve_bin_temp
          self.retrieve_bin_temp = ""
        else:
          self.retrieve_done = True

      print('xor_sum:',xor_sum,'| Vị trí đúng:',pos)
    else:
      print('xor_sum:',xor_sum,'| Vị trí ko đúng:',pos)

  def bin_retrieve_to_string(self):
    
    for i in range(0, len(self.retrieve_bin), 8):
      self.retrieve_message += chr(int(self.retrieve_bin[i:i+8], 2))

  

my_msg = "phan dai, duong truc dong"
wulee = WuleeLastestVersion()
wulee.set_key('minhduc')
wulee.set_cover_image('cat.jpeg')
wulee.set_message(my_msg)
wulee.hide()
# wulee.set_retrieve_max(len(my_msg))
wulee.retrieve()
wulee.compare_test()
# a = wulee.fi_int_to_binary([ord('a')])
# print(a)
# b = wulee.fi_binary_to_int(a)
# print(b)