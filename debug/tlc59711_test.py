# Simple demo of the TLC59711 16-bit 12 channel LED PWM driver.
# Shows setting channel values in a few ways.
# Author: Tony DiCola
import board
import busio
import time

import adafruit_tlc59711


# Define SPI bus connected to chip.  You only need the clock and MOSI (output)
# line to use this chip.
spi = busio.SPI(board.SCK, MOSI=board.MOSI)

# Define the TLC59711 instance.
leds = adafruit_tlc59711.TLC59711(spi)
# Optionally you can disable the auto_show behavior that updates the chip
# as soon as any channel value is written.  The default is True/on but you can
# disable and explicitly call show to control when updates happen for better
# animation or atomic RGB LED updates.
#leds = adafruit_tlc59711.TLC59711(spi, auto_show=False)

# There are a couple ways to control the channels of the chip.
# The first is using an interface like a strip of NeoPixels.  Index into the
# class for the channel and set or get its R, G, B tuple value.  Note the
# component values are 16-bit numbers that range from 0-65535 (off to full
# brightness).  Remember there are only 4 channels available too (0 to 3).
# For example set channel 0 (R0, G0, B0) to half brightness:
#leds[0] = (32767, 32767, 32767)
# Dont forget to call show if you disabled auto_show above.
#leds.show()

# Or to set channel 1 to full red only (green and blue off).
#leds[1] = (65535, 0, 0)

# You can also explicitly control each R0, G0, B0, R1, B1, etc. channel
# by getting and setting its 16-bit value directly with properties.
# For example set channel 2 to full green (i.e. G2 to maximum):
#leds.g2 = 65535
# Again don't forget to call show if you disabled auto_show above.
#leds.show()

# The chip also supports global brightness channels to change the red, green,
# blue colors of all 4 channels at once.  These are 7-bit values that range
# from 0-127.  Get and set them with the red_brightness, green_brightness,
# and blue_brightness properties and again be sure to call show if you
# disabled auto_show.
# For example set the red channel to half brightness globally.
#leds.red_brightness = 63
# Don't forget to call show if you disabled auto_show above.
#leds.show()
#while True:
#    leds.b0 = 32000
while False:
    leds.r2 = 0
    print('off')
    time.sleep(2)
    leds.r2 = 65535
    print('on')
    time.sleep(2)
while True:
    #for i in range(50, 65535, 100):
    #for i in range(1, 65535, 100):
    #    print(i)
    #    leds.g1 = i
    #    leds.g2 = i
    #    leds.g3 = i
    #    leds.r2 = i
    #    leds.b3 = i
    #for i in range(65535, 50, -100):
    #for i in range(65535, 1, -100):
    #    print(i)
    #    leds.r2 = i
    #    leds.b3 = i
    #for i in range(0, 65535, 100):
    #    print((i,i,i))
    #    leds.set_pixel_all((i,i,i))
    #    leds.show()
    #for i in range(65535, 0, -100):
    #    print((i,i,i))
    #    leds.set_pixel_all((i,i,i))
    #    leds.show()
    leds.set_pixel_all((65535, 65535, 65535))
    leds.show()
    for i in range (40000, 0, -100):
        #leds[1] = (0,0,0)
        #leds.set_pixel(1, (i,65000,65000))
        leds.r2 = i
        #leds.g3 = i
        #leds.b3 = i
        #leds.b2 = i
        #leds.set_pixel_all((i, i, i))
        #leds.set_pixel(3, (i,65000,65000))
        leds.show()
