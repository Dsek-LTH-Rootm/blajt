# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# simple demo of the TLC59711 16-bit 12 channel LED PWM driver.
# Shows the minimal usage - how to set pixel values in a few ways.
# Author: Tony DiCola

import board
import busio
import time
import threading

import adafruit_tlc59711

# Define SPI bus connected to chip.
# You only need the clock and MOSI (output) line to use this chip.
spi = busio.SPI(board.SCK, MOSI=board.MOSI)
pixels = adafruit_tlc59711.TLC59711(spi)

# examples how to set the pixels:
# range:
# 0 - 65535
# or
# 0.0 - 1.0
# every pixel needs a color -
# give it just a list or tuple with 3 integer values: R G B

# set all pixels to a very low level
# pixels.set_pixel_all((10, 10, 10))

# every chip has 4 Pixels (=RGB-LEDs = 12 Channel)
# pixels[0] = (100, 100, 100)
# pixels[1] = (0, 0, 100)
# pixels[2] = (0.01, 0.0, 0.01)
# pixels[3] = (0.1, 0.01, 0.0)
# if you are ready to show your values you have to call
# pixels.show()

# there are a bunch of other ways to set pixel.
# have a look at the other examples.
current_colors = {'red': 0, 'green': 0,
                  'blue': 0, 'white_down': 0, 'white_up': 0}

cycle_colors_run = False


def normalize(color):
    return 65535 - color*257


def set_all_colors(red, green, blue, white_down, white_up):
    global cycle_colors_run
    # maybe we also need to wait on confirmation that cycle thread has stopped
    cycle_colors_run = False

    current_colors['red'] = red
    current_colors['green'] = green
    current_colors['blue'] = blue
    current_colors['white_down'] = white_down
    current_colors['white_up'] = white_up

    pixels.r0 = normalize(blue)
    pixels.b1 = normalize(white_up)
    pixels.b2 = normalize(white_down)
    pixels.r2 = normalize(green)
    pixels.b3 = normalize(red)
    pixels.show()


def get_all_colors():
    return current_colors


def clear():
    global cycle_colors_run
    # maybe we also need to wait on confirmation that cycle thread has stopped
    cycle_colors_run = False
    set_all_colors(0, 0, 0, 0, 0)


def run_cycle_colors():
    global cycle_colors_run
    HSVlights = [0, 4, 8, 13, 17, 21, 25, 30, 34, 38, 42, 47, 51, 55, 59, 64, 68, 72, 76,
                 81, 85, 89, 93, 98, 102, 106, 110, 115, 119, 123, 127, 132, 136, 140, 144,
                 149, 153, 157, 161, 166, 170, 174, 178, 183, 187, 191, 195, 200, 204, 208,
                 212, 217, 221, 225, 229, 234, 238, 242, 246, 251, 255]

    def HSV_approx(angle):
        angle = int(angle) % 360

        if (angle < 60):
            r = 255
            g = HSVlights[angle]
            b = 0
        elif (angle < 120):
            r = HSVlights[120 - angle]
            g = 255
            b = 0
        elif (angle < 180):
            r = 0
            g = 255
            b = HSVlights[angle - 120]
        elif (angle < 240):
            r = 0
            g = HSVlights[240 - angle]
            b = 255
        elif (angle < 300):
            r = HSVlights[angle - 240]
            g = 0
            b = 255
        else:
            r = 255
            g = 0
            b = HSVlights[360 - angle]
        return (r/255, g/255, b/255)

    def new_hue(old_hue):
        speed = 0.001

        if abs(old_hue - 1/6) < 0.02 or abs(old_hue - 3/6) < 0.02 or abs(old_hue - 5/6) < 0.02:
            speed /= 2

        new_hue = old_hue + speed
        if new_hue >= 1:
            new_hue = 0
        return new_hue

    pixels.b2 = 65535
    hue_offset = 0
    while cycle_colors_run:
        color = HSV_approx(hue_offset*360)

        r = int((1.0 - color[0])*65535)
        g = int((1.0 - color[1])*65535)
        b = int((1.0 - color[2])*65535)
        pixels.b3 = r
        pixels.r2 = g
        pixels.r0 = b
        pixels.show()

        hue_offset = new_hue(hue_offset)


def cycle_colors():
    global cycle_colors_run
    run_cycle_colors()
    if cycle_colors_run:
        cycle_colors_run = False
    else:
        cycle_colors_run = True
        cycle_thread = threading.Thread(
            target=run_cycle_colors, args=()).start()
