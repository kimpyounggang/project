   if howhp == False:#class how_hp:
        #캡처할 좌표를 담아둔다
        hp_img_left_top = (450,5)
        hp_img_right_bottom = (554,45)

        #좌측상단의 x, 우측하단의 y값을 저장해둔다
        hp_img_left_top_x = hp_img_left_top[0]
        hp_img_right_bottom_y = hp_img_right_bottom[1]

        #캡쳐 범위의 폭과 높이를 구한다
        capture_width = 80
        capture_height = 35

        """ 
        capture_width = hp_img_right_bottom[0]-hp_img_left_top[0]
        capture_height = hp_img_right_bottom[1]-hp_img_left_top[1]
        """

        #캡쳐 경로와 이름을 지정한다
        try:
            os.remove('temp/hp.png')
        except:
            pass

        cap_hp = 'temp/hp.png'
        #스크린샷
        pag.screenshot(cap_hp, region=(hp_img_left_top_x, hp_img_right_bottom_y, capture_width, capture_height))


        # 이미지 불러오기, 리사이즈, Gray 프로세싱 
        image = cv2.imread('temp/hp.png')
        #res = cv2.resize(image, dsize=(200, 100), interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

        # write the grayscale image to disk as a temporary file so we can # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장. 

        filename = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename, gray) 

        # Simple image to string 

        text = pytesseract.image_to_string(Image.open(filename), lang=None) 
        os.remove(filename) 

        #now_hp = text
        now_hp = re.findall('\d+', text)

        #리스트를 문자열로 변환
        now_hp = ''.join(now_hp)
        print("nowhp: "+now_hp)

        #문자열을 정수형으로 변환
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
                howhp = True
            else:
                print("굶주림 이상무")
                howhp = True
        except:
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
            howhp = True

    if howmp == False:#class how_mp:
            
        #캡처할 좌표를 담아둔다
        mp_img_left_top = (630,5)
        mp_img_right_bottom = (754,45)

        #좌측상단의 x, 우측하단의 y값을 저장해둔다
        mp_img_left_top_x = mp_img_left_top[0]
        mp_img_right_bottom_y = mp_img_right_bottom[1]

        #캡쳐 범위의 폭과 높이를 구한다
        capture_width = 80
        capture_height = 35

        #캡쳐 경로와 이름을 지정한다
        try:
            os.remove('temp/mp.png')
        except:
            pass

        cap_mp = 'temp/mp.png'
        #스크린샷
        pag.screenshot(cap_mp, region=(mp_img_left_top_x, mp_img_right_bottom_y, capture_width, capture_height))


        # 이미지 불러오기, 리사이즈, Gray 프로세싱 
        image = cv2.imread('temp/mp.png')
        #res = cv2.resize(image, dsize=(200, 100), interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

        # write the grayscale image to disk as a temporary file so we can # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장. 

        filename = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename, gray) 

        # Simple image to string 

        text = pytesseract.image_to_string(Image.open(filename), lang=None) 
        os.remove(filename) 

        #now_mp = text
        now_mp = re.findall('\d+', text)
        
        #리스트를 문자열로 변환
        now_mp = ''.join(now_mp)
        print("nowmp: "+now_mp)

        #문자열을 정수형으로 변환
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
                howmp = True
            else:
                print("물 이상무")
                howmp = True
        except:
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
            howmp = True
   
    if howen == False:# class how_energy:
        
        #캡처할 좌표를 담아둔다
        en_img_left_top = (52,5)
        en_img_right_bottom = (154,45)

        #좌측상단의 x, 우측하단의 y값을 저장해둔다
        en_img_left_top_x = en_img_left_top[0]
        en_img_right_bottom_y = en_img_right_bottom[1]

        #캡쳐 범위의 폭과 높이를 구한다
        capture_width = 80
        capture_height = 35

        #캡쳐 경로와 이름을 지정한다
        try:
            os.remove('temp/en.png')
        except:
            pass

        cap_en = 'temp/en.png'
        #스크린샷
        pag.screenshot(cap_en, region=(en_img_left_top_x, en_img_right_bottom_y, capture_width, capture_height))


        # 이미지 불러오기, 리사이즈, Gray 프로세싱 
        image = cv2.imread('temp/en.png')
        #res = cv2.resize(image, dsize=(200, 100), interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

        # write the grayscale image to disk as a temporary file so we can # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장. 

        filename = 'temp/{}.png'.format(os.getpid()) 
        cv2.imwrite(filename, gray) 

        # Simple image to string 

        text = pytesseract.image_to_string(Image.open(filename), lang=None) 
        os.remove(filename) 

        #now_mp = text
        now_en = re.findall('\d+', text)
        #리스트를 문자열로 변환
        now_en = ''.join(now_en)
        print("nowen: "+now_en)

        try:
            if int(now_en) < 50:
                print("에너지가 낮음")
            else:
                print("에너지 이상무")
                howen = True
        except:
            pass

    if howstm == False:
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

    if howhp == True:
        if howmp == True:
            if howen == True:
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
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
                filename = 'temp/{}.png'.format(os.getpid()) 
                cv2.imwrite(filename, gray) 
                text = pytesseract.image_to_string(Image.open(filename), lang='kor')
                os.remove(filename) 
                now_cut = text
                if "나무" in now_cut:
                    print("자르는중")
                    time.sleep(15)
                else:
                    if "자르기" in now_cut:
                        print("자르는중")
                        time.sleep(15)   

