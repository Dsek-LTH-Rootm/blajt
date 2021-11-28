#!/usr/bin/python3

from bottle import run, get, post, request, route, template
#from controller import set_color, set_all, cycle_colors

@route('/')
def index():
    return template('<b> Blajt says hello</b>!')

@post('/cycle_colors')
def cycle():
    #cycle_colors()
    return "Cycling colors"

@post('/set_color')
def set_light_colors():
    pixel = request.forms.get('pixel')
    red = request.forms.get('red')
    green = request.forms.get('green')
    blue = request.forms.get('blue')

    #set_color(pixel, red, green, blue)
    return template("Setting colors ({{red}}, {{green}}, {{blue}}) on pixel {{pixel}}", red=red, green=green, blue=blue, pixel=pixel)

@post('/set_all_colors')
def set_all_colors():
    red = request.forms.get('red')
    green = request.forms.get('green')
    blue = request.forms.get('blue')

    #set_all(red, green, blue)
    return template("Setting all pixels to colors ({{red}}, {{green}}, {{blue}})", red=red, green=green, blue=blue)

run(host='localhost', port=8080)
