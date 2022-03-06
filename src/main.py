#!/usr/bin/python3

from bottle import run, get, post, request, route, template
import controller

@route('/')
def index():
   return '''
      <form action="/set_all_colors" method="post">
        Red: <input name="red" type="number" /></br>
        Green: <input name="green" type="number" /></br>
        Blue: <input name="blue" type="number" /></br>
        White Down: <input name="white_down" type="number" /></br>
        White Up: <input name="white_up" type="number" /></br>
        <input value="Set color" type="submit" />
      </form>
   '''

@post('/cycle_colors')
def cycle():
    #cycle_colors()
    return "Cycling colors"

@post('/set_color')
def set_light_colors():
    pixel = int(request.forms.get('pixel'))
    red = int(request.forms.get('red'))
    green = int(request.forms.get('green'))
    blue = int(request.forms.get('blue'))

    set_color(pixel, red, green, blue)
    return template("Setting colors ({{red}}, {{green}}, {{blue}}) on pixel {{pixel}}", red=red, green=green, blue=blue, pixel=pixel)

@post('/set_all')
def set_all():
    red = int(request.forms.get('red'))
    green = int(request.forms.get('green'))
    blue = int(request.forms.get('blue'))

    set_all(red, green, blue)
    return template("Setting all pixels to colors ({{red}}, {{green}}, {{blue}})", red=red, green=green, blue=blue)

@post('/set_all_colors')
def set_all_colors():
    red = int(request.forms.get('red'))
    green = int(request.forms.get('green'))
    blue = int(request.forms.get('blue'))
    white_down = int(request.forms.get('white_down'))
    white_up = int(request.forms.get('white_up'))

    controller.set_all_colors(red, green, blue, white_down, white_up)
    return template("Setting all pixels to colors ({{red}}, {{green}}, {{blue}}, {{white_down}}, {{white_up}})", red=red, green=green, blue=blue, white_down=white_down, white_up=white_up)


run(host='0.0.0.0', port=8080)
