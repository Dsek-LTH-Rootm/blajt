# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# simple demo of the TLC59711 16-bit 12 channel LED PWM driver.
# Shows the minimal usage - how to set pixel values in a few ways.
# Author: Tony DiCola

import board
import busio
import time

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


def normalize(color):
    return 65535 - color*255


def set_all_colors(red, green, blue, white_down, white_up):
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
    set_all_colors(0, 0, 0, 0, 0)


def cycle_colors():
    pixels.show()
