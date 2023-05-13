import pwmio
import board
import time

led = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)
while True:
    for i in range(100):
        led.duty_cycle = int(65535 / 100 * i)
        time.sleep(0.01)
    for i in range(100):
        led.duty_cycle = int(65535 / 100 * (100 - i))
        time.sleep(0.01)
