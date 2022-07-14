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
import keyboard


# 설치한 tesseract 프로그램 경로 (64비트) 
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


time.sleep(2)
start=False

while True:

    try:
#굶주림체크
        hp_img_left_top = (450,5)
        hp_img_right_bottom = (554,45)
        hp_img_left_top_x = hp_img_left_top[0]
        hp_img_right_bottom_y = hp_img_right_bottom[1]
        capture_width_hp = 80
        capture_height_hp = 35
        try:
            os.remove('temp/hp.png')
        except:
            pass
        cap_hp = 'temp/hp.png'
        pag.screenshot(cap_hp, region=(hp_img_left_top_x, hp_img_right_bottom_y, capture_width_hp, capture_height_hp))
        image = cv2.imread('temp/hp.png')
        gray_hp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        filename_hp = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename_hp, gray_hp) 
        text_hp = pytesseract.image_to_string(Image.open(filename_hp), lang=None) 
        os.remove(filename_hp)
        now_hp = re.findall('\d+', text_hp)
        now_hp = ''.join(now_hp)
        print("nowhp: "+now_hp)
        try:
            if int(now_hp) < 50:
                print("굶주림 낮음")
                #어디 눌러져있는지 모르니 한번 초기화
                pag.click(311, 703)
                time.sleep(0.2)
                #가방
                pag.click(796, 718)
                time.sleep(0.2)
                #소고기캔
                pag.click(605, 452)
                time.sleep(0.2)
                #먹기버튼
                pag.click(960, 317)
                time.sleep(0.2)
                print("밥먹음")
                
            else:
                print("굶주림 이상무")
                
        except:
            print("굶주림 수치 검색안됨")
            pag.click(450, 61)

            hp_img_left_top = (440,85)
            hp_img_right_bottom = (554,100)
            hp_img_left_top_x = hp_img_left_top[0]
            hp_img_right_bottom_y = hp_img_right_bottom[1]
            capture_width_hp = 120
            capture_height_hp = 35
            try:
                os.remove('temp/hp.png')
            except:
                pass
            cap_hp = 'temp/hp.png'
            pag.screenshot(cap_hp, region=(hp_img_left_top_x, hp_img_right_bottom_y, capture_width_hp, capture_height_hp))
            image = cv2.imread('temp/hp.png')
            gray_hp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            filename_hp = 'temp/{}.png'.format(os.getpid()) 
            cv2.imwrite(filename_hp, gray_hp) 
            text_hp = pytesseract.image_to_string(Image.open(filename_hp), lang=None) 
            os.remove(filename_hp)
            now_hp = re.findall('\d+', text_hp)
            now_hp = ''.join(now_hp)
            now_hp = now_hp[:-3]
            print("nowhp: "+now_hp)
            try:
                if int(now_hp) < 50:
                    print("굶주림 낮음")
                    #어디 눌러져있는지 모르니 한번 초기화
                    pag.click(311, 703)
                    time.sleep(0.2)
                    #가방
                    pag.click(796, 718)
                    time.sleep(0.2)
                    #소고기캔
                    pag.click(605, 452)
                    time.sleep(0.2)
                    #먹기버튼
                    pag.click(960, 317)
                    time.sleep(0.2)
                    print("밥먹음")
                else:
                    print("굶주림 이상무")
            except:
                pass

            
#목마름체크
        #################################################################
        mp_img_left_top = (630,5)
        mp_img_right_bottom = (754,45)
        mp_img_left_top_x = mp_img_left_top[0]
        mp_img_right_bottom_y = mp_img_right_bottom[1]
        capture_width_mp = 80
        capture_height_mp = 35
        try:
            os.remove('temp/mp.png')
        except:
            pass
        cap_mp = 'temp/mp.png'
        #스크린샷
        pag.screenshot(cap_mp, region=(mp_img_left_top_x, mp_img_right_bottom_y, capture_width_mp, capture_height_mp))
        image = cv2.imread('temp/mp.png')
        gray_mp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        filename_mp = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename_mp, gray_mp) 
        text_mp = pytesseract.image_to_string(Image.open(filename_mp), lang=None) 
        os.remove(filename_mp) 
        now_mp = re.findall('\d+', text_mp)
        now_mp = ''.join(now_mp)
        print("nowmp: "+now_mp)

        try:
            if int(now_mp) < 50:
                print("물이 낮음")
                #어디 눌러져있는지 모르니 한번 초기화
                pag.click(311, 703)
                time.sleep(0.2)
                #가방
                pag.click(796, 718)
                time.sleep(0.2)
                #물
                pag.click(370, 212)
                time.sleep(0.2)
                #먹기버튼
                pag.click(960, 317)
                time.sleep(0.2)
                print("물 먹음")
                
            else:
                print("물 이상무")
                
        except:
            print("물 수치 검색안됨")
            pag.click(638,58)
            mp_img_left_top = (620,85)
            mp_img_right_bottom = (780,100)
            mp_img_left_top_x = mp_img_left_top[0]
            mp_img_right_bottom_y = mp_img_right_bottom[1]
            capture_width_mp = 120
            capture_height_mp = 35
            try:
                os.remove('temp/mp.png')
            except:
                pass
            cap_mp = 'temp/mp.png'
            #스크린샷
            pag.screenshot(cap_mp, region=(mp_img_left_top_x, mp_img_right_bottom_y, capture_width_mp, capture_height_mp))
            image = cv2.imread('temp/mp.png')
            gray_mp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            filename_mp = 'temp/{}.png'.format(os.getpid()) 
            cv2.imwrite(filename_mp, gray_mp) 
            text_mp = pytesseract.image_to_string(Image.open(filename_mp), lang=None) 
            os.remove(filename_mp) 
            now_mp = re.findall('\d+', text_mp)
            now_mp = ''.join(now_mp)
            now_mp = now_mp[:-3]
            print("nowmp: "+now_mp)
            try:
                if int(now_mp) < 50:
                    print("물이 낮음")
                    #어디 눌러져있는지 모르니 한번 초기화
                    pag.click(311, 703)
                    time.sleep(0.2)
                    #가방
                    pag.click(796, 718)
                    time.sleep(0.2)
                    #물
                    pag.click(370, 212)
                    time.sleep(0.2)
                    #먹기버튼
                    pag.click(960, 317)
                    time.sleep(0.2)
                    print("물 먹음")
                    
                else:
                    print("물 이상무")
            except:
                pass
            # #어디 눌러져있는지 모르니 한번 초기화
            # pag.click(311, 703)
            # time.sleep(0.2)
            # #가방
            # pag.click(796, 718)
            # time.sleep(0.2)
            # #물
            # pag.click(370, 212)
            # time.sleep(0.2)
            # #먹기버튼
            # pag.click(960, 317)
            # time.sleep(0.2)
            # print("물 먹음")
            
#스테미나체크
        ##############################################################
        stm_img_left_top = (800,5)
        stm_img_right_bottom = (954,45)
        stm_img_left_top_x = stm_img_left_top[0]
        stm_img_right_bottom_y = stm_img_right_bottom[1]
        capture_width_stm = 80
        capture_height_stm = 35
        try:
            os.remove('temp/stm.png')
        except:
            pass
        cap_stm = 'temp/stm.png'
        pag.screenshot(cap_stm, region=(stm_img_left_top_x, stm_img_right_bottom_y, capture_width_stm, capture_height_stm))
        image = cv2.imread('temp/stm.png')
        gray_stm = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        filename_stm = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename_stm, gray_stm) 
        text_stm = pytesseract.image_to_string(Image.open(filename_stm), lang=None) 
        os.remove(filename_stm)
        now_stm = re.findall('\d+', text_stm)
        now_stm = ''.join(now_stm)
        print("nowstm: "+now_stm)
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
                
            else:
                print("스테미나 이상무")
               
        except:
            print("스테미나 검색안됨")
            # print("스테미나 낮음")
            # #어디 눌러져있는지 모르니 한번 초기화
            # pag.click(311, 703)
            # time.sleep(0.2)
            # #제작탭
            # pag.click(1185,712)
            # time.sleep(0.2)
            # #모닥불
            # pag.click(693,258)
            # time.sleep(0.2)
            # #손으로불피우기
            # pag.click(364,315)
            # time.sleep(10)
            # print("불 피움")
            

#피통체크
        #########################################################
        en_img_left_top = (52,5)
        en_img_right_bottom = (154,45)
        en_img_left_top_x = en_img_left_top[0]
        en_img_right_bottom_y = en_img_right_bottom[1]
        capture_width_en = 80
        capture_height_en = 35
        try:
            os.remove('temp/en.png')
        except:
            pass
        cap_en = 'temp/en.png'
        pag.screenshot(cap_en, region=(en_img_left_top_x, en_img_right_bottom_y, capture_width_en, capture_height_en))
        image = cv2.imread('temp/en.png')
        gray_en = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filename_en = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename_en, gray_en) 
        text_en = pytesseract.image_to_string(Image.open(filename_en), lang=None) 
        os.remove(filename_en) 
        now_en = re.findall('\d+', text_en)
        now_en = ''.join(now_en)
        print("nowen: "+now_en)
        try:
            if int(now_en) < 50:
                print("에너지가 낮음")
                start=False
            else:
                print("에너지 이상무")
                start=True
        except:
            pass

        if start==True:
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
            cut_img_left_top = (419,250)
            cut_img_right_bottom = (701,355)
            cut_img_left_top_x = cut_img_left_top[0]
            cut_img_right_bottom_y = cut_img_right_bottom[1]
            capture_width = 300
            capture_height = 80
            try:
                os.remove('temp/cut.png')
            except:
                pass
            cap_hp = 'temp/cut.png'
            pag.screenshot(cap_hp, region=(cut_img_left_top_x, cut_img_right_bottom_y, capture_width, capture_height))
            image = cv2.imread('temp/cut.png')
            gray_cut = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
            filename_cut = 'temp/{}.png'.format(os.getpid()) 
            cv2.imwrite(filename_cut, gray_cut) 
            text_cut = pytesseract.image_to_string(Image.open(filename_cut), lang='kor')
            os.remove(filename_cut) 
            now_cut = text_cut
            if "나무" in now_cut:
                print("자르는중")
                time.sleep(15)
            else:
                if "자르기" in now_cut:
                    print("자르는중")
                    time.sleep(15)   
    
    except:
        # pag.click(294, 717)
        # time.sleep(1)
        # pag.click(294, 717)
        # time.sleep(1)
        # if keyboard.is_pressed('a'):
        #     print("탈출!")
        pass


#cv2.imshow("Image", image) 
#cv2.waitKey(0)
