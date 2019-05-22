from microbit import *
import random


score = 0
number = random.randint(1, 10)
display.show(str(number))


while True:
    if button_a.is_pressed():
        next_number = random.randint(1, 10)
        if number <= next_number:
            display.show(Image.HAPPY)
            sleep(400)
            score = score + 1
            number = next_number
            next_number = random.randint(1, 10)
            sleep(100)
            display.show(str(number))
        elif number >= next_number:
            display.show(Image.SAD)
            sleep(400)
            display.scroll(str(score))
            sleep(500)
            break
        
    if button_b.is_pressed():
        next_number = random.randint(1, 10)
        if number >= next_number:
            display.show(Image.HAPPY)
            sleep(400)
            score = score + 1
            number = next_number
            next_number = random.randint(1, 10)
            sleep(100)
            display.show(str(number))
        elif number <= next_number:
            display.show(Image.SAD)
            sleep(400)
            display.scroll(str(score))
            sleep(500)
            break
