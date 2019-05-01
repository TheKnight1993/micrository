from microbit import *
import random

num_1 = Image("00000:00000:00900:00000:00000:")

num_2 = Image("00000:09000:00000:00090:00000:")

num_3 = Image("00000:09000:00900:00090:00000:")

num_4 = Image("00000:09090:00000:09090:00000:")

num_5 = Image("00000:09090:00900:09090:00000:")

num_6 = Image("00000:09090:09090:09090:00000:")

def dice():
    number = random.randint(1, 6)
    if number == 1:
        display.show(num_1)
        sleep(100)
    elif number == 2:
        display.show(num_2)
        sleep(100)
    elif number == 3:
        display.show(num_3)
        sleep(100)
    elif number == 4:
        display.show(num_4)
        sleep(100)
    elif number == 5:
        display.show(num_5)
        sleep(100)
    elif number == 6:
        display.show(num_6)
        sleep(100)
    return

while True:
    if button_a.is_pressed():
        dice()
        sleep(500)
        dice()
        sleep(500)
        dice()
        sleep(500)
        dice()
        sleep(500)
        dice()
        sleep(500)
        dice()
        sleep(500)
        dice()
        sleep(500)
        dice()
        sleep(500)