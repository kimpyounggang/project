from sys import flags
import pyautogui as pag
from PIL import ImageGrab, ImageFilter, Image
import time
import mouse
import cv2 

# 캡쳐할 영역의 왼쪽 상단 모서리와 오른쪽 하단 모서리의 좌표값을 미리구해둔다.

# while True:
#     if mouse.is_pressed("left"):
#         pos = mouse.get_position()
#         print(pag.position())
#         time.sleep(1)

# =9, y=153)
# Point(x=779, y=645)

# im = Image.open('image/water.png')
# blurImage = im.filter(ImageFilter.CONTOUR)
# blurImage.save('image/waterpython-blur.png')
# five_btn = pag.locateOnScreen('image/waterpython-blur.PNG')
# print(five_btn)

# image = cv2.imread('image/waterpython-blur.png')
# cv2.imshow("blurImage",image)

# cv2.waitKey(0)

#pag.moveTo(522, 168)

#(502, 18)294, 413