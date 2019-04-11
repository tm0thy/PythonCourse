from numpy import *
from cs50 import *


def CountField(figure,x,y=None):

    if figure=='kolo':
        pole=pi*x**2
        return pole
    elif figure=='prostokat':
        pole=x*y
        return pole
    else:
        pole=x*y/2
        return pole

figure = get_string('Podaj figure: ')
figure = figure.lower()

fig=['kolo','prostokat','romb','trojkat']
while True:
    if figure in fig:
        break
    else:
        figure = get_string('Podaj figure: ')
        figure = figure.lower()


x = get_float('podaj x: ')
while x <= 0:
    x = get_float('podaj x: ')
y = 0
if figure != 'kolo':
    y = get_float('podaj y: ')
    while y <= 0:
        y = get_float('podaj: ')

print('pole figury: ',"%.2f" % CountField(figure,x,y))