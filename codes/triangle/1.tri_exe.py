#Code by Durga prasad
#December 6, 2019
#released under GNU GPL
#Drawing a right angled triangle

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
#import subprocess
#import shlex
#end if

#Sides
a = 4
c = 3
#Triangle vertices
C = np.array([a,c]) 
B = np.array([a,0]) 
A = np.array([0,0])
P=np.array([5,0]) 
m = A-C
n = np.matmul(omat,m) 
N=np.vstack((m,n))
p = np.zeros(2)
p[0] = m@P
p[1] = n@A
#Intersection
M=np.linalg.inv(N.T)@p
print(M)
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_MP = line_gen(M,P)
x_BP = line_gen(B,P)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_MP[0,:],x_MP[1,:],label='$MP$')
plt.plot(x_BP[0,:],x_BP[1,:],label='$BP$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A(0,0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 +0.03), B[1] * (1) , 'B(4,0)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(4,3)')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P(5,0)')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 -0.15), M[1] * (1 - 0.03) , 'M(3.2,2.4)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('../../figs/triangle/2.tri_exercise.pdf')
plt.savefig('../../figs/triangle/1.tri_exercise.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_polar.pdf"))
#else
plt.show()







