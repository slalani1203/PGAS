import time
import board
import neopixel
import random
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A7, echo_pin=board.A6)

BRIGHTNESS = 1
num_pixels = 30
np = neopixel.NeoPixel(board.A1, num_pixels, brightness=BRIGHTNESS, auto_write=False)

def light():
    np.fill([0, 0, 0])
    ranging = 30 - (sonar.distance/5)
    for i in range(int(ranging)):
        if ranging >= 0 and ranging <= 10:
            np[i] = [171, 0, 0]
        if ranging >= 11 and ranging <= 20:
            np[i] = [255, 238, 0]
        if ranging >= 21 and ranging <= 30:
            np[i] = [56, 231, 0]
    np.show()
    time.sleep(0.001)

while True:
    try:
        light()
    except RuntimeError:
        pass
    time.sleep(0.1)
