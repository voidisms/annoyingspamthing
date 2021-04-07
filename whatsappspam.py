from pynput.keyboard import Key, Controller
import time

#Can also work for other stuff, this was only intended for WhatsApp but it can work for anything really
message = "Spam message"
keyboard = Controller()

time.sleep(5)


for num in range(100):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    
