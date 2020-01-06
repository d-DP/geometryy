import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if


len = 50
r1 = 5
a=4
c=3
b=np.sqrt(a**2+c**2)
x=np.sqrt(b**2-a**2)
A = np.array([-c,a]) 
B = np.array([c,a]) 
O=np.array([0,0])
N=np.array([0,-x])
M = np.array([0,a]) 
D=np.array([a,-c])
C=np.array([-a,-c])

theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O).T
#Generating all lines
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)
x_ON = line_gen(O,N)
x_OM = line_gen(O,M)
x_OB = line_gen(O,B)
x_OD = line_gen(O,D)
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')



#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_ON[0,:],x_ON[1,:],label='$ON$')
plt.plot(x_OM[0,:],x_OM[1,:],label='$OM$')
plt.plot(x_OB[0,:],x_OB[1,:],label='$OB$')
plt.plot(x_OD[0,:],x_OD[1,:],label='$OD$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(-3,4)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(3,4)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(-4,-3)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D(4,-3)')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.03), M[1] * (1 - 0.1) , 'M(0,4)')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.03), O[1] * (1 - 0.1) , 'O(0,0)')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 + 0.03), N[1] * (1 - 0.1) , 'N(0,-3)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../figs/misc.pdf')
plt.savefig('../figs/misc.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()
