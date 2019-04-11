from numpy import *
from cs50 import*



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

###################################################################################
Figure=[]
Numbers=[]
for i in range(2):
    print(i+1,' figura: ')
    figure = get_string('Podaj figure: ')
    figure = figure.lower()

    fig=['kolo','prostokat','romb','trojkat']
    while True:
        if figure in fig:
            break
        else:
            figure = get_string('Podaj figure: ')
            figure = figure.lower()
    Figure.append(figure)

    x = get_float('podaj x: ')
    while x <= 0:
        x = get_float('podaj x: ')
    y = 0
    if figure != 'kolo':
        y = get_float('podaj y: ')
        while y <= 0:
            y = get_float('podaj: ')
    Numbers.append([x,y])
###################################################################################
Field=[]

for i in range(2):
    a=CountField(Figure[i],Numbers[i][0],Numbers[i][1])
    Field.append(a)

if Field[0]>Field[1]:
    print('wieksze pole to: ',"%.2f"%Field[0],' nalezy do ',Figure[0])
else:
    print('wieksze pole to: ',"%.2f"%Field[1],' nalezy do ',Figure[1])
