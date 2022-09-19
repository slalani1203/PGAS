import board
import neopixel
import time
import random

BRIGHTNESS = .25
num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)

def chase(color1, color2, loop, count, delay):
    result = 0
    for i in range(count * loop):
        np.fill(color1)
        for k in range(num_pixels):
            if k % count == result:
                np[k] = color2
        np.show()
        time.sleep(delay)
        result += 1
        result %= count

def sparkle(color1, color2, delay, loop):
    for i in range(loop):
        np.fill(color1)
        np.show()
        Spark1 = random.randint(0, 9)
        Spark2 = random.randint(0, 9)
        Spark3 = random.randint(0, 9)
        np[Spark1] = color2
        np[Spark2] = color2
        np[Spark3] = color2
        np.show()
        time.sleep(delay)

while True:
    sparkle([255, 115, 0], [255, 60, 0], 0.05, 10)
    chase([255, 115, 0], [255, 60, 0], 1, 3, 0.1)
