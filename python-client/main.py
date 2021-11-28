#!/usr/bin/python3

from bottle import run, get, post, request, route, template
from controller import set_color, set_all, cycle_colors

@route('/')
def index():
   return '''
      <form action="/set_all_colors" method="post">
        Red: <input name="red" type="number" /></br>
        Green: <input name="green" type="number" /></br>
        Blue: <input name="blue" type="number" /></br>
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

@post('/set_all_colors')
def set_all_colors():
    red = int(request.forms.get('red'))
    green = int(request.forms.get('green'))
    blue = int(request.forms.get('blue'))

    set_all(red, green, blue)
    return template("Setting all pixels to colors ({{red}}, {{green}}, {{blue}})", red=red, green=green, blue=blue)

run(host='192.168.7.241', port=8080)
