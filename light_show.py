import board
import neopixel
import time
import random

BRIGHTNESS = .25
num_pixels = 10
np = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, brightness=BRIGHTNESS, auto_write=False)

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
        np.fill(color1)
        for k in range(num_pixels):
            if k % count == result:
                np[k] = color2
        np.show()
        time.sleep(delay)
        result += 1
        result %= count

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
Function name: fade_out_specific
Description: This is a light show that fades out a specific singular pixel
Parameters: color - rgb value that fades out; increment - the time that the light 
is delayed/stays on; pix_num - the specific pixel on the board that will complete the function
Return value: none
"""
def fade_out_specific(color, increment, pix_num):
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
        np[pix_num] = ((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

"""
Function name: fade_out
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
Function name: fade_in_specific
Description: This is a light show that fades in a specific singular pixel
Parameters: color - rgb value that fades in; increment - the time that the light 
is delayed/stays on; pix_num - the specific pixel on the board that will complete the function
Return value: none
"""
def fade_in_specific(color, increment, pix_num):
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
        np[pix_num] = ((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)
# purple
mycolor1 = [67, 17, 85]
# orange
mycolor2 = [223, 109, 0]
# red
mycolor3 = [170, 26, 26]
# light orange
mycolor4 = [255, 186, 128]
# yellow
mycolor5 = [225, 185, 0]
# green 
mycolor6 = [99, 194, 21]
# blue
mycolor7 = [23, 92, 140]
# violet
mycolor8 = [32, 3, 44]

# the show will be on a infinite loop
while True:
    # chase show 1
    fade_in(mycolor1, 0.01)
    np.fill(mycolor1)
    fade_in_specific(mycolor2, 0.01, 0)
    np[0] = (mycolor2)
    fade_in_specific(mycolor2, 0.01, 3)
    np[3] = (mycolor2)
    fade_in_specific(mycolor2, 0.01, 6)
    np[6] = (mycolor2)
    fade_in_specific(mycolor2, 0.01, 9)
    np[9] = (mycolor2)
    chase(mycolor1, mycolor2, 10, 3, 0.1)
    fade_out_specific(mycolor2, 0.01, 0)
    fade_in_specific(mycolor1, 0.01, 0)
    np[0] = (mycolor1)
    fade_out_specific(mycolor2, 0.01, 2)
    fade_in_specific(mycolor1, 0.01, 2)
    np[2] = (mycolor1)
    fade_out_specific(mycolor2, 0.01, 5)
    fade_in_specific(mycolor1, 0.01, 5)
    np[5] = (mycolor1)
    fade_out_specific(mycolor2, 0.01, 8)
    fade_in_specific(mycolor1, 0.01, 8)
    np[8] = (mycolor1)
    fade_out(mycolor1, 0.01)
    # sparkle show
    fade_in(mycolor3, 0.01)
    sparkle(mycolor3, mycolor1, 0.1, 25)
    fade_out(mycolor3, 0.01)
    fade_in(mycolor4, 0.01)
    sparkle(mycolor4, mycolor8, 0.1, 50)
    fade_out(mycolor4, 0.01)
    fade_in(mycolor7, 0.01)
    sparkle(mycolor7, mycolor3, 0.1, 100)
    fade_out(mycolor7, 0.01)
    fade_in(mycolor5, 0.01)
    sparkle(mycolor5, mycolor2, 0.1, 50)
    fade_out(mycolor5, 0.01)
    fade_in(mycolor6, 0.01)
    sparkle(mycolor6, mycolor4, 0.1, 25)
    fade_out(mycolor6, 0.01)
    # chase 2 show
    fade_in(mycolor7, 0.01)
    np.fill(mycolor7)
    fade_in_specific(mycolor5, 0.01, 0)
    np[0] = (mycolor5)
    fade_in_specific(mycolor5, 0.01, 3)
    np[3] = (mycolor5)
    fade_in_specific(mycolor5, 0.01, 6)
    np[6] = (mycolor5)
    fade_in_specific(mycolor5, 0.01, 9)
    np[9] = (mycolor5)
    chase(mycolor7, mycolor5, 10, 3, 0.1)
    fade_out_specific(mycolor5, 0.01, 0)
    fade_in_specific(mycolor7, 0.01, 0)
    np[0] = (mycolor1)
    fade_out_specific(mycolor5, 0.01, 2)
    fade_in_specific(mycolor7, 0.01, 2)
    np[2] = (mycolor7)
    fade_out_specific(mycolor5, 0.01, 5)
    fade_in_specific(mycolor7, 0.01, 5)
    np[5] = (mycolor7)
    fade_out_specific(mycolor5, 0.01, 8)
    fade_in_specific(mycolor7, 0.01, 8)
    np[8] = (mycolor7)
    fade_out(mycolor7, 0.01)
    # repeats at the end
