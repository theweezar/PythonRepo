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
    self.hidden_count = 0   # số tin đã giấu 
    self.retrieve_message = "" # tin nhắn đã trích xuất
    self.retrieve_count = 0    # số tin nhắn đã trích xuất
    self.retrieve_max = 0      # số tin trích xuất tối đa
    self.CHANNEL_BLUE = 0      
    self.CHANNEL_GREEN = 1
    self.CHANNEL_RED = 2

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
    print('Word: \''+ key_string +'\' turn into:')
    print(self.key)
    
  def set_key_to_null(self):
    self.key = None
  
  # Các thao tác với biến -------------------------------
  def set_message(self, message):
    self.message = message

  def set_cover_image(self, path):
    self.cover_image = cv2.imread(path)
    # self.cover_image = np.array(Image.open(path))
    # self.cover_image.flags.writeable = True
    # print(dir(self.cover_image))

  def save_stego_image(self, file_name):
    cv2.imwrite(file_name, self.cover_image)

  def set_retrieve_max(self, retrieve_max):
    self.retrieve_max = retrieve_max

  def reset_when_hide_done(self):
    self.message = ""
    self.hidden_count = 0

  def reset_when_retrieve_done(self):
    self.retrieve_count = 0
    self.retrieve_max = 0
    self.retrieve_message = ""

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

  def hide(self):
    self.hide_in_channel(self.CHANNEL_BLUE)
    self.hide_in_channel(self.CHANNEL_GREEN)
    self.hide_in_channel(self.CHANNEL_RED)

  def fi_bin_random_replace(self, fi_bin, target, replace):
    for i in range(0, fi_bin.shape[0]):
      for j in range(0, fi_bin.shape[1]):
        if fi_bin[i, j] == target and self.key[i, j] == 1:
          fi_bin[i, j] = replace
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
  
  def hide_in_block_int(self, block_int):
    char_to_hide = self.message[self.hidden_count]
    bin_char_to_hide = '{0:08b}'.format(ord(char_to_hide))
    # Duyệt theo cột của block int
    for i in range(0,self.block_width):
      # Lấy hết giá trị dọc trong cột thứ i
      fi =  block_int[:,i]
      fi_bin = self.fi_int_to_binary(fi)
      # SUM ( fi & key )
      and_sum = np.bitwise_and(fi_bin, self.key).sum()
      # SUM ( key )
      key_sum = self.key.sum()

      if and_sum > 0 and and_sum < key_sum:
        if and_sum % 2 == int(bin_char_to_hide[i]):
          continue
        elif and_sum == 1:
          fi_bin = self.fi_bin_random_replace(fi_bin, 0, 1)
        elif and_sum == key_sum - 1:
          fi_bin = self.fi_bin_random_replace(fi_bin, 1, 0)
        else:
          fi_bin = self.fi_bin_random_reverse(fi_bin)
      
      fi = self.fi_binary_to_int(fi_bin)
      # print(block_int)
      # print(block_int[:, i])
      # print(fi)
      block_int[:,i] = fi
    
    return block_int
      

  def hide_in_channel(self, channel):
    # Trích xuất Channel
    img_channel = self.cover_image[:,:,channel]
    # Duyệt hết ảnh
    # Duyệt theo chiều cao ( height ) khóa
    for i in range(0, self.get_cover_image_height(), self.block_height) :  
      for j in range(0, self.get_cover_image_width(), self.block_width ) :
        block_int = img_channel[i:i+self.block_height, j: j+self.block_width]
        
        if self.hidden_count == len(self.message):
          return
        
        # Đặt ra giới hạn cho những block có kích thước không đủ
        if block_int.shape[0] == self.block_height and block_int.shape[1] == self.block_width:
          block_int = self.hide_in_block_int(block_int)
          img_channel[i:i+self.block_height, j: j+self.block_width] = block_int
          self.hidden_count += 1

  def retrieve(self):
    self.retrieve_in_channel(self.CHANNEL_BLUE)
    self.retrieve_in_channel(self.CHANNEL_GREEN)
    self.retrieve_in_channel(self.CHANNEL_RED)

  def retrieve_in_channel(self, channel):
    # Trích xuất Channel
    img_channel = self.cover_image[:,:,channel]
    # Duyệt hết ảnh
    # Duyệt theo chiều cao ( height ) khóa
    for i in range(0, self.get_cover_image_height(), self.block_height) :  
      for j in range(0, self.get_cover_image_width(), self.block_width ) :
        block_int = img_channel[i:i+self.block_height, j: j+self.block_width]
        
        if self.retrieve_count == self.retrieve_max:
          return
        
        # Đặt ra giới hạn cho những block có kích thước không đủ
        if block_int.shape[0] == self.block_height and block_int.shape[1] == self.block_width:
          block_int = self.retrieve_in_block_int(block_int)
          self.retrieve_count += 1

  def retrieve_in_block_int(self, block_int):
    bin_char = ""

    for i in range(0, self.block_width):
      fi = block_int[:, i]
      fi_bin = self.fi_int_to_binary(fi)
      # SUM ( fi & key )
      and_sum = np.bitwise_and(fi_bin, self.key).sum()
      # SUM ( key )
      key_sum = self.key.sum()

      if and_sum > 0 and and_sum < key_sum:
        if and_sum % 2 == 0:
          bin_char += "0"
        else:
          bin_char += "1"

    self.retrieve_message += chr(int(bin_char, 2))
    self.retrieve_count += 1
    return

  

# wulee = WuleeLastestVersion()
# wulee.set_key('duc')
# wulee.set_cover_image('extract.png')
# wulee.set_message('test new version')
# wulee.hide()
# wulee.set_retrieve_max(5)
# wulee.retrieve()
# print(wulee.retrieve_message)
# wulee.save_stego_image(