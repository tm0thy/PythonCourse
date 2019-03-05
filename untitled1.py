# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:10:09 2019

@author: Tymek
"""

from math import factorial
import numpy as np
import matplotlib.pyplot as plt

print('#1')
x=[]
y=[]

for i in range(45):
    x.append(56+i)
    
    y.append(2*(x[i])**2 + 2*x[i]+2)
    
print(y)

print('#2')


a=int(input('Choose a number:'))
print('factorial:',factorial(a))

print('#3')

array=list()

number=input('Number of elements:')
print('enter numbers:')
for i in range(int(number)):
    n=input()
    array.append(int(n))
    
lowest=array[0]
for i in range(int(number)):
    if array[i]< lowest:
        lowest=array[i]
index=[i for i, j in enumerate(array) if j==lowest]

print('lowest number/s: ', lowest)
print('index of this number/s: ',index)

print('#4')
      
start=int(input('start:'))
end=int(input('end:'))

if start==end:
    print('dont do it')
    while end==start:
        end=int(input('end:'))

X=np.linspace(start,end,1000)
Y=4*np.sin(X/2)

plt.plot(X,Y)
plt.show()
