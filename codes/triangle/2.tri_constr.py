#Code by P.Durga Prasad
#December 27, 2019
import numpy as np
import matplotlib.pyplot as plt

from coeffs import *

#if using termux
#import subprocess
#import shlex
#end if
k=3.5

#Sides
a = 8
d=45
AngleB=(np.pi/180)*(d)
b = (-(2*a*k*np.cos(AngleB))+(a)**2+(k)**2)/(-(2*k)+(2*a*(np.cos(AngleB))))
print(b)
c=k+b
print(c)
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p)
c=k+b
print(q)
#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
A
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.03) , 'A(8.48,8.48)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(0,0)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(8,0)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('../../figs/triangle/2.tri_construction.pdf')
plt.savefig('../../figs/triangle/2.tri_construction.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_right_angle.pdf"))
#else
plt.show()







