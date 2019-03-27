import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import *


###############################################################################

print('#1')
print('First circle:')
X=get_float()
while X<=0:
    print('number must be greater than 0:')
    X=get_float()

perimetrerX = 2*np.pi *X
fieldX= np.pi*X**2
print('perimeter: ',perimetrerX,'field: ',fieldX)

print('Second circle:')
Y=get_float()
while Y<=0:
    print('number must be greater than 0:')
    Y=get_float()

perimetrerY = 2*np.pi *Y
fieldY = np.pi*Y**2
print('perimeter: ',perimetrerY,'field: ',fieldY)

#################################################################################

print('#2')

print('x: ')
x=get_float()

print('y: ')
y=get_float()

while y==0:
    print('you cant divide by 0, type y: ')
    y = get_float()
if x%y==0 and x%2==0 and y%2==0:
    print('x is divisible by y and both are even')
    print(x/y)
else:
    print('One of the numbers is not even or x is not divisible by y')
    print(x/y)

#########################################################################

print('#3')

a= get_float('x: ')
b = get_float('y: ')
while b == 0:
    print('you cant divide by 0')
    b = get_float('y: ')

print('X is divisable by Y' if a % b == 0 else 'X is NOT divisable by Y')
print(a/b)

##########################################################################


print('#4')

c = get_float('x: ')
d = get_float('y: ')
while d == 0:
    print('you cant divide by 0')
    d = get_float('y: ')

print('X is divisable by Y' if c % d == 0 else 'X is NOT divisable by Y')
print("X/Y is: ",round(c/d,2))

##########################################################################

print('#5')


value = get_float("value: ")

x_knots = np.linspace(-3*np.pi,3*np.pi,201)
y_knots = np.linspace(-3*np.pi,3*np.pi,201)
A, B = np.meshgrid(x_knots,y_knots)
R = np.sqrt(A**2 + B**2)/value
Z = np.cos(R)**(3+value)*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize = (8,5)))
ax.plot_surface(A,B,Z,rstride = 1,cstride = 1,cmap = plt.cm.viridis,linewidth = 3.5)
plt.show()