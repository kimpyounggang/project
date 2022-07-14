import cv2 
import os
try: from PIL import Image,ImageGrab
except ImportError: 
    import Image
import pytesseract 
import pyautogui as pag
import numpy as np
import re
import time
import keyboard


# 설치한 tesseract 프로그램 경로 (64비트) 
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def check_status(left_top, right_bottom, file, who,lang_a,capture_width,capture_height):
    try:
        img_left_top = (left_top)
        img_right_bottom = (right_bottom)
        img_left_top_x = img_left_top[0]
        img_right_bottom_y = img_right_bottom[1]
        capture_width
        capture_height
        try:
            os.remove(file)
        except:
            pass
        cap = file
        pag.screenshot(cap, region=(img_left_top_x, img_right_bottom_y, capture_width, capture_height))
        image = cv2.imread(file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        filename = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename, gray) 
        text = pytesseract.image_to_string(Image.open(filename), lang=lang_a) 
        os.remove(filename)
        if file=='temp/cut.png':
            now = text
            return now
        else:    
            now = re.findall('\d+', text)
            now = ''.join(now)
            print(who+" "+now)
            return now
    except:
        pass


def fill_status(tem):
    ##이미지 검색을 위해서
    entire = ImageGrab.grab()
    entire.save('temp/entire.png')

    # 입력이미지와 템플릿 이미지 읽기
    img = cv2.imread('temp/entire.png')
    template = cv2.imread(tem)
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
        #print(method_name, min_val, max_val, min_loc, max_loc)

        # TM_SQDIFF의 경우 최소값이 좋은 매칭, 나머지는 그 반대 ---③
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
            match_val = min_val
        else:
            top_left = max_loc
            match_val = max_val
        # 매칭 좌표 구해서 사각형 표시   ---④      
        # bottom_right = (top_left[0] + tw, top_left[1] + th)
        # cv2.rectangle(img_draw, top_left, bottom_right, (0,0,255),2)
        
        
        # 매칭 포인트 표시 ---⑤
        # cv2.putText(img_draw, str(match_val), top_left, \
        #             cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0), 1, cv2.LINE_AA)
        #cv2.imshow(method_name, img_draw)
    print(min_loc)
    return min_loc
    


  

hp_left_top = (450,5)
hp_right_bottom = (554,45)
hp_file = 'temp/hp.png'
hp_who = "Now HP"


mp_left_top = (630,5)
mp_right_bottom = (754,45)
mp_file = 'temp/mp.png'
mp_who = "Now MP"


stm_left_top = (800,5)
stm_right_bottom = (954,45)
stm_file = 'temp/stm.png'
stm_who = "Now stm"

en_left_top = (52,5)
en_right_bottom = (154,45)
en_file = 'temp/en.png'
en_who = "Now en"

cut_left_top = (419,250)
cut_right_bottom = (701,355)
cut_file = 'temp/cut.png'
cut_who = " "
cut_capture_width = 300
cut_capture_height = 80
    

while True:
    ##상태체크
    capture_width = 80
    capture_height = 35
    now_hp = check_status(hp_left_top,hp_right_bottom,hp_file,hp_who,None,capture_width,capture_height)
    try:
        if int(now_hp) < 50:
            print("상태:배고픔")
            #어디 눌러져있는지 모르니 한번 초기화
            pag.click(311, 703)
            time.sleep(0.2)
            #돋보기
            pag.click(994,698)
            time.sleep(0.2)
            tem_hp='image/apple.png'
            food_xy = fill_status(tem_hp)
            pag.click(food_xy)
            time.sleep(0.2)
            pag.click(960, 370)
            time.sleep(0.2)
            print("행동:밥먹음")
    except:
        print("상태:배고픔 검색안됨")
        pag.click(450,61)
        now_hp = check_status((440,85),(554,100),hp_file,hp_who,None,120,35)
        now_hp = now_hp[:-3]
        print(now_hp)
        if int(now_hp) < 50:
            print("상태:배고픔")
            #어디 눌러져있는지 모르니 한번 초기화
            pag.click(311, 703)
            time.sleep(0.2)
            #돋보기
            pag.click(994,698)
            time.sleep(0.2)
            tem_hp='image/apple.png'
            food_xy = fill_status(tem_hp)
            pag.click(food_xy)
            time.sleep(0.2)
            pag.click(960, 370)
            time.sleep(0.2)
            print("행동:밥먹음")


    now_mp = check_status(mp_left_top,mp_right_bottom,mp_file,mp_who,None,capture_width,capture_height)
    try:
        if int(now_mp) < 50:
            print("상태:목마름")
            #어디 눌러져있는지 모르니 한번 초기화
            pag.click(311, 703)
            time.sleep(0.2)
            #돋보기
            pag.click(994,698)
            time.sleep(0.2)
            tem_mp='image/water_back.png'
            water_xy = fill_status(tem_mp)
            pag.click(water_xy)
            time.sleep(0.2)
            pag.click(960, 300)
            time.sleep(0.2)
            print("행동:물먹음")
    except:
        print("상태:목마름 검색안됨")
        pag.click(638,58)
        now_mp = check_status((620,85),(780,100),hp_file,hp_who,None,120,35)
        now_mp = now_mp[:-3]
        print(now_mp)
        if int(now_mp) < 50:
            print("상태:목마름")
            #어디 눌러져있는지 모르니 한번 초기화
            pag.click(311, 703)
            time.sleep(0.2)
            #돋보기
            pag.click(994,698)
            time.sleep(0.2)
            tem_mp='image/water_back.png'
            water_xy = fill_status(tem_mp)
            pag.click(water_xy)
            time.sleep(0.2)
            pag.click(960, 300)
            time.sleep(0.2)
            print("행동:물먹음")


    now_stm = check_status(stm_left_top,stm_right_bottom,stm_file,stm_who,None,capture_width,capture_height)

    now_en = check_status(en_left_top,en_right_bottom,en_file,en_who,None,capture_width,capture_height)
    try:
        if int(now_en) < 40:
            print("상태:딸피")
            print("오류감지 매크로종료")
            break
    except:
        pass

    #어디 눌러져있는지 모르니 한번 초기화
    pag.click(311, 703)
    time.sleep(0.2)
    #돋보기
    pag.click(994,698)
    time.sleep(0.2)
    #나무자르기
    pag.click(1150,600)
    time.sleep(0.2)
    #레버
    pag.click(817,585)
    time.sleep(0.2)
    #확인
    pag.click(914,577)
    time.sleep(5)
    cut = check_status(cut_left_top,cut_right_bottom,cut_file,cut_who,'kor',300,80)
    if "나무" in cut:
        print("자르는중")
        time.sleep(15)
    else:
        if "자르기" in cut:
            print("자르는중")
            time.sleep(15)
    
    
    
