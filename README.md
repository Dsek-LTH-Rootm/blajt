# blajt
Blajt is a service to control the bar LED-strips in iDét.

Above the bar, there is one purely white LED-strip. By the floor in front of the bar, there are 4 strips of different colors, red, green, blue, and white. Each strip can be set seperately.

# Endpoints
 - **GET /get_all_colors**: Returns a JSON-object describing the current value(0-255) of each light.
 - **POST /set_all_colors**: Takes a form with values between 0-255 for each strip(**red**, **green**, *blue**, **white_up**, and **white_down**) and sets the colors.
 - **POST /clear**: Turns all LED-strips off.
 
As an example, the command below sets the lights below the bar to dataråsa, and the white light above the bar to full power:

`curl -X POST blajt:8080/set_all_colors -H "Content-Type: application/x-www-form-urlencoded" -d "red=242&green=128&blue=161&white_down=0&white_up=255"`
# HW
 - Raspberry Pi Zero W
 - Adafruit TLC59711 PWM controller
 - 5 x IRF520NPBF N-channel MOSFETs

## Kopplingsschema
TODO

# Prereqs
 - [Installera CircuitPython](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)
 - [Aktivera SPI](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/)
 - [Installera libb för TLC59711](https://github.com/adafruit/Adafruit_CircuitPython_TLC59711)
