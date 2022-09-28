import board
import neopixel
import time
import random


BRIGHTNESS = 1
num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)


"""
Function name: fire
Description: Amplified sparkle seqeuence that flashes at random intensitys.
Parameters: Color1-RGB value that is the background;Color2 -RGB value that sparkles; Loop-amount of time it repeats
Return value: none
"""
def fire(color1, color2, loop):
    for j in range(loop):
        intensity = random.random() * 0.5 + 0.1
        background = [int(i * intensity) for i in color1]
        np.fill(background)
        for i in range(random.randint(1, int(num_pixels/3))):
            intensity = random.random() * 0.5 + 0.1
            foreground = [int(i * intensity) for i in color2]
            np[random.randint(0, num_pixels-1)] = foreground
        np.show()
        time.sleep(0.08)

"""
Function name: lightning
Description: Amplified sparkle seqeuence that flashes at random intensitys.
Parameters: Color1-RGB VALUE that is the background;Color2 -RGB value that sparkles; Loop-amount of time it repeats
Return value: none
"""
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

"""
Function name: strike
Description: Strike is a lightshow that flashes a random amount of times at random intensitys.
Parameters: Color - RGB Value
Return value: none
"""
def strike(color):
    sec = random.random() / 15
    loop = random.randint(3,5)
    for i in range(loop):
        intensity = random.random() * 0.3 + 0.5
        light = [int(i * intensity) for i in color]
        np.fill(color)
        np.show()
        time.sleep(sec)
        np.fill([0,0,0])
        np.show()
        time.sleep(sec)

"""
Function name: fade_out
Description: This is a light show that fades out the color that is inputted into the function
Parameters: color - rgb value that fades out; increment - the amount of time the light is delayed
Return value: none
"""
def fade_out(color, increment):
    rgb = color
    maximum = max (rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = rgb
    while r >= 0 and g >= 0 and b >= 0:
        r -= r_inc
        g -= g_inc
        b -= b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

"""
Function name: fade_in
Description: This is a light show that fades in the color that is inputted into the function
Parameters: color - rgb value that fades in; increment - the amount of time the light is delayed
Return value: none
"""
def fade_in(color, increment):
    rgb = color
    r, g, b = rgb
    r_final = r
    g_final = g
    b_final = b
    print(r_final, g_final, b_final)
    maximum = max(rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = 0, 0, 0
    while r <= r_final and g <= g_final and b <= b_final:
        r += r_inc
        g += g_inc
        b += b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

"""
Function name: chase
Description: This is a light show that sets every nth value as a different color and
spins the colors for a certain amount of time
Parameters: color1 - rgb value that serves as the background; color2 - the nth rgb color
that spins around; loop - int value that repeats the function i times; count - the int nth
value; delay - the amount of time the function stays on
Return value: none
"""
def chase(color1, color2, loop, count, delay):
    result = 0
    for i in range(count * loop):
        intensity = random.random() * 0.3 + 0.5
        filling = [int(i * intensity) for i in color1]
        np.fill(filling)
        for k in range(num_pixels):
            if k % count == result:
                np[k] = color2
        np.show()
        time.sleep(delay)
        result += 1
        result %= count

"""
Function name: pulse
Description: This is a lightshow that repeats a inputed amount of loops. In this case it flashes twice.
Parameters: color - rgb value; Delay - The time is delayed; loop - int value that repeats the function i times;
Return value: none
"""
def pulse(color, delay, loop):
    for i in range(loop):
        for i in range(2):
            np.fill(color)
            np.show()
            time.sleep(delay)
            np.fill([0, 0, 0])
            np.show()
            time.sleep(delay)
            np.show()
        time.sleep(delay * 10)

"""
Function name: sparkle
Description: This is a light show that randomly sets the second color on another pixel
Parameters: color1 - rgb value that serves as the background; color2 - the random rgb color;
loop - int value that repeats the function i times; delay - the amount of time the function
stays on
Return value: none
"""
def sparkle(color1, color2, delay, loop):
    for i in range(loop):
        np.fill(color1)
        np.show()
        for i in range(int(num_pixels/3)):
            Spark1 = random.randint(0, 9)
            np[Spark1] = color2
            np.show()
            time.sleep(delay)


# ongoing loop of light show
while True:
   loop = random.randint(75, 100)
   lightning([34, 2, 56], [104, 52, 139], loop)
   strike([203, 175, 223])
   fire([255, 91, 0], [255, 20, 1], 100)
   np.fill([255, 91, 0])
   time.sleep(1)
   fade_out([255, 91, 0], 0.01)
   fade_in([11, 23, 0], 0.01)
   chase([11, 23, 0], [81, 170, 7], 25, 3, 0.1)
   pulse([71, 71, 100], 0.1, 7)
   sparkle([34, 2, 56], [255,122,12], 0.157, 50)
