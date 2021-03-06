import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

def block_int_to_bin(block):
  arr_bin = ['{0:08b}'.format(int(e)) for e in block]
  np_bin = []
  for a in arr_bin:
    r = [int(b) for b in a]
    np_bin.append(r)
  return np.array(np_bin)

def block_bin_to_int(block):
  int_block = np.array([int(b, 2) for b in [''.join([str(c) for c in e]) for e in block]])
  return int_block

class Wulee:

  def __init__(self):
    # super().__init__()
    self.cover_image = self.message = self.key = self.stego_image = None

  def setCoverImage(self, path):
    self.cover_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    return self

  def setStegoImage(self, path):
    self.stego_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  
  def setMessage(self, message):
    self.message = message
    return self
  
  def setKey(self, key):
    self.key = key
    return self

  def hide_in_block(self, block, word):
    # Kí tự từ dạng char sang dạng binary
    bin_word = '{0:08b}'.format(ord(word))
    print('Block:\n',block,'\nSecret word:',word,'====>',bin_word)
    # 1 block sẽ có 8 cột số, ta duyệt từng cột
    for i in range(0,8):
      # trích xuất 1 cột có chiều dài = 8
      fi = block_int_to_bin(block[:,i])
      # SUM(fi and key)
      and_sum = np.bitwise_and(fi, self.key).sum()
      # SUM(key)
      key_sum = self.key.sum()
      print('\nSUM(fi and key):',and_sum,'| SUM(key):',key_sum,'| Bit:',bin_word[i])
      if and_sum > 0 and and_sum < key_sum:
        if and_sum % 2 == int(bin_word[i]):
          print('====> Do nothing')
        elif and_sum == 1:
          replace = False
          for y in range(0,8):
            for x in range(0,8):
              if fi[y,x] == 0 and key[y,x] == 1:
                fi[y,x] = 1
                block[:,i] = block_bin_to_int(fi)
                replace = True
                break
              if replace is True:
                break
          print('====> and_sum == 1')
        elif and_sum == key_sum - 1:
          replace = False
          for y in range(0,8):
            for x in range(0,8):
              if fi[y,x] == 1 and self.key[y,x] == 1:
                fi[y,x] = 0
                block[:,i] = block_bin_to_int(fi)
                replace = True
                break
              if replace is True:
                break
          print('====> and_sum == key_sum - 1')
        else:
          replace = False
          for y in range(0,8):
            for x in range(0,8):
              if self.key[y,x] == 1:
                if fi[y,x] == 1:
                  fi[y,x] = 0
                else:
                  fi[y,x] = 1
                block[:,i] = block_bin_to_int(fi)
                replace = True
                break
              if replace is True:
                break
          print('====> Everything else')
    print('\nNew Block:\n', block)
    return block
  
  def hide(self):
    # Kiểm tra đầu vô của ảnh gốc, dữ liệu cần dấu, khóa
    if self.cover_image is None:
      print('No cover image')
    elif self.message is None:
      print('No message')
    elif self.key is None:
      print('No key')
    else:
      h = self.cover_image.shape[0]
      w = self.cover_image.shape[1]
      # word_hidden là số lượng kí tự đã dấu, khi bắt đầu là 0
      word_hidden = 0
      # Khi dấu tin xong thì done = True
      done = False
      # Duyệt chiều dài trước, chiều rộng sau, bước nhảy bằng 8 vì có 8 bit
      for i in range(0, h, 8):
        for j in range(0, w, 8):
          # trích xuất 1 block có shape = (8,8)
          block = self.cover_image[i:i+8,j:j+8]
          # Nếu block đó ko đủ dài hay rộng thì bỏ qua tìm block mới
          if block.shape[0] == 8 and block.shape[1] == 8:
            # Bắt đầu quá trình dấu 1 kí tự vào 1 block
            block = self.hide_in_block(block, self.message[word_hidden])
            # Gán block đó vào trong ảnh gốc
            self.cover_image[i:i+8,j:j+8] = block
            word_hidden += 1
          if word_hidden == len(self.message):
            done = True
            break
        if done is True:
          break
      print("Hidden successfully")
    return self
  
  def retrieve_in_block(self, block):
    print('Retrieve in block:\n',block)
    bin_message = ''
    for i in range(0,8):
      fi = block_int_to_bin(block[:,i])
      # SUM(fi and key)
      and_sum = np.bitwise_and(fi, self.key).sum()
      # SUM(key)
      key_sum = self.key.sum()
      print('\nSUM(fi and key):',and_sum,'| SUM(key):',key_sum)
      if and_sum > 0 and and_sum < key_sum:
        if and_sum % 2 == 0:
          bin_message += "0"
        else:
          bin_message += "1"
    s_msg = chr(int(bin_message,2))
    print("Secret bin:",bin_message," | Character:", s_msg)
    return s_msg

  def retrieve(self):
    hidden_msg = ''
    # Chiều dài của msg
    d = 10
    h = self.cover_image.shape[0]
    w = self.cover_image.shape[1]
    for i in range(0, h, 8):
      for j in range(0, w, 8):
        block = self.cover_image[i:i+8,j:j+8]
        if block.shape[0] == 8 and block.shape[1] == 8:
          # Bắt đầu quá trình trích xuất 1 kí tự tin nhắn bí mật
          hidden_msg += self.retrieve_in_block(block)
          d -= 1
        if d == 0:
          break
      if d == 0:
        break
    print('Hidden message is:',hidden_msg)
    return self

  

  def saveStegoImage(self):
    cv2.imwrite('stego.jpg', self.cover_image)
    return self


wulee = Wulee()

the_key = np.array([
            [1,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,1,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,1,0,1,0,1,0,0]
        ])

wulee.setCoverImage('cat.jpeg').setMessage('ducdeptrai').setKey(the_key).hide().saveStegoImage().retrieve()

# wulee.setCoverImage('stego.jpg').setKey(the_key).retrieve()