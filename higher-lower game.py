from microbit import *
import random




while True:
    score = 0
    number = random.randint(1-10)
    display.show(str(number))
    if button_a.is_pressed():
        next_number = random.randint(1-10)
        if number <= next_number:
            display.show(image.HAPPY)
            score = score + 1
            number = next_number
            next_number = random.randint(1-10)
            sleep(100)
            display.show(str(number))
        elif number >= next_number:
            display.show(image.SAD)
            sleep(400)
            display.scroll(str(score))
            sleep(500)
            break
    if button_b.is_pressed():
        next_number = random.randint(1-10)
        if number >= next_number:
            display.show(image.HAPPY)
            score = score + 1
            number = next_number
            next_number = random.randint(1-10)
            sleep(100)
            display.show(str(number))
        elif number <= next_number:
            display.show(image.SAD)
            sleep(400)
            display.scroll(str(score))
            sleep(500)
            break
