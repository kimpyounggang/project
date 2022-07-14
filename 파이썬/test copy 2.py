from PIL import ImageGrab
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

#인벤토리 전체화면

# #캡처할 좌표를 담아둔다
# hp_img_left_top = (20,0)
# hp_img_right_bottom = (770,150)
# #좌측상단의 x, 우측하단의 y값을 저장해둔다
# hp_img_left_top_x = hp_img_left_top[0]
# hp_img_right_bottom_y = hp_img_right_bottom[1]
# #캡쳐 범위의 폭과 높이를 구한다
# capture_width = 760
# capture_height = 520
# #캡쳐 경로와 이름을 지정한다
# try:
#     os.remove('temp/entire.png')
# except:
#     pass
# cap_hp = 'temp/entire.png'
# #스크린샷
# pag.screenshot(cap_hp, region=(hp_img_left_top_x, hp_img_right_bottom_y, capture_width, capture_height))




# 이미지 불러오기, 리사이즈, Gray 프로세싱 
# image = cv2.imread('temp/entire.png')

# #res = cv2.resize(image, dsize=(200, 100), interpolation=cv2.INTER_CUBIC)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# # write the grayscale image to disk as a temporary file so we can # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장. 

# filename = 'temp/{}.png'.format(os.getpid()) 
# cv2.imwrite(filename, gray) 

# # Simple image to string 

# text = pytesseract.image_to_string(Image.open(filename), lang=None) 
# os.remove(filename) 

# five_btn = pag.locateOnScreen('image/water_back.PNG')
# print(five_btn)






#cv2.imshow("Image", Image) 
#cv2.waitKey(0)

entire = ImageGrab.grab()
entire.save('temp/entire.png')

# 입력이미지와 템플릿 이미지 읽기
img = cv2.imread('temp/entire.png')
template = cv2.imread('image/water_back.png')
th, tw = template.shape[:2]
# cv2.imshow('template', template)

# 3가지 매칭 메서드 순회
methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', \
                                     'cv2.TM_SQDIFF_NORMED']
for i, method_name in enumerate(methods):
    img_draw = img.copy()
    method = eval(method_name)
    # 템플릿 매칭   ---①
    res = cv2.matchTemplate(img, template, method)
    # 최대, 최소값과 그 좌표 구하기 ---②
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(method_name, min_val, max_val, min_loc, max_loc)

    # TM_SQDIFF의 경우 최소값이 좋은 매칭, 나머지는 그 반대 ---③
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val
    # 매칭 좌표 구해서 사각형 표시   ---④      
    bottom_right = (top_left[0] + tw, top_left[1] + th)
    cv2.rectangle(img_draw, top_left, bottom_right, (0,0,255),2)
    
    
    # 매칭 포인트 표시 ---⑤
    cv2.putText(img_draw, str(match_val), top_left, \
                cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0), 1, cv2.LINE_AA)
    #cv2.imshow(method_name, img_draw)


pag.moveTo(min_loc)
print(min_loc)
cv2.waitKey(0)
cv2.destroyAllWindows()    