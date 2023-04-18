import pyautogui as pg
import random
import time
import webbrowser

sub = int(input("Enter how many sub you want: "))

url = str(input("Enter you channel URL: "))

sb = url + "?sub_confirmation=1"

for i in range(sub):

    #Name & Email Generator

    UP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOW = "abcdefghijklmnopqrstuvwxyz"

    sps = UP + LOW

    LP = 8

    NE = "".join(random.sample(sps, LP))

    #CODE 1 For name email password

    webbrowser.open_new('https://www.youtube.com')

    time.sleep(10)

    time.sleep(5)

    pg.moveTo(820, 65)
    pg.click()
    pg.typewrite("https://www.youtube.com/channel_switcher")
    pg.press('Enter')

    time.sleep(10)

    pg.moveTo(645, 300)
    pg.click()

    time.sleep(5)

    pg.moveTo(860, 625)
    pg.click()
    time.sleep(2)
    pg.typewrite(NE)

    time.sleep(2)

    pg.moveTo(600, 695)
    pg.click()

    time.sleep(2)

    pg.moveTo(1010, 785)
    pg.click()

    time.sleep(10)

    pg.moveTo(820, 65)
    pg.click()
    time.sleep(2)
    pg.typewrite(sb)
    pg.press('Enter')
    time.sleep(5)
    pg.moveTo(1118, 622, 3)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
