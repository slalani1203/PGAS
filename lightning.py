import board
import time
import neopixel
import random

num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=1.0, auto_write=False)


def lightning(color1, color2, loop):
    for j in range(loop):
        intensity = random.random() * 0.2 + 0.3
        background = [int(i * intensity) for i in color1]
        np.fill(background)
        for i in range(random.randint(1, int(num_pixels/3))):
            intensity = random.random() * 0.8 + 0.2
            foreground = [int(i * intensity) for i in color2]
            np[random.randint(0, num_pixels-1)] = foreground
        np.show()
        time.sleep(0.08)

def strike(color):
    sec = random.random() / 25
    loop = random.randint(1,4)
    for i in range(loop):
        intensity = random.random() * 0.3 + 0.5
        light = [int(i * intensity) for i in color]
        np.fill(color)
        np.show()
        time.sleep(sec)
        np.fill([0,0,0])
        np.show()
        time.sleep(sec)

while True:
    loop = random.randint(25, 100)
    lightning([34, 2, 56], [104, 52, 139], loop)
    strike([203, 175, 223])
