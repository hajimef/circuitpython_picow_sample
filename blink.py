import digitalio
import board
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
while True:
    print("On")
    led.value = True
    time.sleep(0.5)
    print("Off")
    led.value = False
    time.sleep(0.5)
