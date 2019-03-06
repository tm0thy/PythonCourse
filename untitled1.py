# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:10:09 2019

@author: Tymek
"""


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

def fact(number):
    result=1
    for i in range(number):
        result*=i+1
    return result
    
print('factorial:',fact(a))

print('#3')

array=list()
index=[]

number=int(input('Number of elements:'))
print('enter numbers:')
for i in range(number):
    n=input()
    array.append(int(n))
    
def lowest(tab):
    low=tab[0]
    index=[]
    for i in tab:
        if i<low:
            low=i
    for i in range(len(tab)):
        if low==tab[i]:
            index.append(i)
    return low,index


print('lowest number/s: ', lowest(array)[0])
print('index of this number/s: ', lowest(array)[1])

print('#4')
      
start=int(input('start:'))
end=int(input('end:'))

if start==end:
    print('dont do it')
    while end==start:
        end=int(input('end:'))

X=np.linspace(start,end,1000)
Y=np.cos(X) * np.exp(-(X/2.0)**2)

plt.plot(X,Y)
plt.show()
