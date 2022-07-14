import cv2 
import os
try: from PIL import Image 
except ImportError: 
    import Image 
import pytesseract 
import pyautogui as pag
import numpy as np
import re
import time

# 설치한 tesseract 프로그램 경로 (64비트) 
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

stm_img_left_top = (800,5)
stm_img_right_bottom = (954,45)
stm_img_left_top_x = stm_img_left_top[0]
stm_img_right_bottom_y = stm_img_right_bottom[1]
capture_width = 80
capture_height = 35
try:
    os.remove('temp/stm.png')
except:
    pass
cap_stm = 'temp/stm.png'
pag.screenshot(cap_stm, region=(stm_img_left_top_x, stm_img_right_bottom_y, capture_width, capture_height))
image = cv2.imread('temp/stm.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
filename = 'temp/{}.png'.format(os.getpid()) 
cv2.imwrite(filename, gray) 
text = pytesseract.image_to_string(Image.open(filename), lang=None) 
os.remove(filename)
now_stm = re.findall('\d+', text)
now_stm = ''.join(now_stm)
print("nowstm: "+now_stm)
if int(now_stm) < 50:
    print("스테미나 낮음")
    print(now_stm)
    howstm = False

#문자열을 정수형으로 변환
try:
    if int(now_stm) < 20:
        print("스테미나 낮음")
        #어디 눌러져있는지 모르니 한번 초기화
        pag.click(311, 703)
        time.sleep(0.2)
        #제작탭
        pag.click(1185,712)
        time.sleep(0.2)
        #모닥불
        pag.click(693,258)
        time.sleep(0.2)
        #손으로불피우기
        pag.click(364,315)
        time.sleep(10)
        print("불 피움")
        howstm = True
    else:
        print("스테미나 이상무")
        howstm = True
except:
    print("스테미나 낮음")
    #어디 눌러져있는지 모르니 한번 초기화
    pag.click(311, 703)
    time.sleep(0.2)
    #제작탭
    pag.click(1185,712)
    time.sleep(0.2)
    #모닥불
    pag.click(693,258)
    time.sleep(0.2)
    #손으로불피우기
    pag.click(364,315)
    time.sleep(10)
    print("불 피움")
    howstm = True
