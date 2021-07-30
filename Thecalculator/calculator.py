import math
from typing import Text
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.config  import Config




def proces():
    x = int(input('Enter first number:'))
    function = input('Enter a function(+,*,/,-):')
    y = int(input('Enter a second number:'))

    if function == '+' :
        print(x + y)

    if function == '*' :
        print(x * y)

    if function == '-' :
        print(x - y)

    if function == '/':
        print(x / y)


Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')

class Thewidget(Widget):
    pass

class Thecalculator(App):
    pass

Thecalculator().run()









