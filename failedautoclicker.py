import pynput.mouse    as ms
import pynput.keyboard as kb
import time
print("Paste the URL of the Youtube video here: ")
url = input()
url = list(url)
print(url)
formattedurl = ""
for i in range(len(url)):
    if i > 11:
        formattedurl += url[i]
print(formattedurl)
time.sleep(1)
mouse = ms.Controller()
keyboard = kb.Controller()
mouse.position = (1179, 1031)
time.sleep(0.3)
mouse.press(ms.Button.left)
mouse.release(ms.Button.left)
time.sleep(0.3)
mouse.position = (137, 0)
time.sleep(0.3)
mouse.press(ms.Button.left)
mouse.release(ms.Button.left)
time.sleep(0.3)
mouse.position = (211, 35)
time.sleep(0.3)
mouse.press(ms.Button.left)
mouse.release(ms.Button.left)
time.sleep(0.3)
for i in range(2):
    mouse.position = (1000, 60)
    time.sleep(0.3)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)
    time.sleep(0.3)
    keyboard.type("www.savethevideo.com/convert")
    time.sleep(0.3)
    keyboard.press(kb.Key.enter)
    keyboard.release(kb.Key.enter)
    time.sleep(0.8) 
    mouse.position = (728, 328)
    time.sleep(0.3)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)
    time.sleep(0.3)
    keyboard.type("https")
    with keyboard.pressed(kb.Key.shift):
        keyboard.press(';')
        keyboard.release(';')
    keyboard.type("//www." + formattedurl)
    time.sleep(0.3)
    mouse.position = (840, 380)
    time.sleep(0.3)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)
    time.sleep(0.3)
    mouse.position = (880, 550)
    time.sleep(0.3)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)
    time.sleep(0.5)
    mouse.position = (660, 480)
    time.sleep(0.5)
    mouse.press(ms.Button.left)
    mouse.release(ms.Button.left)
    time.sleep(0.3)




