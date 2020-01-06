#Code by GVV Sharma
#December 7, 2019
#released under GNU GPL
#Drawing a parallelogram  given 2 sides and a diagonal
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
#import subprocess
#import shlex
#end if


#Triangle sides
#a = 6
#b = 4.5
#c = 7.5
a = 5
b = 6
angD = np.pi/180*120
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angD))





#Parallelogram vertices
D = np.array([-5,0]) 
B = np.array([5,0]) 
C = np.array([0,3]) 
A = np.array([0,-3])
P=(A+B)/2
Q=(B+C)/2
R=(D+C)/2
S=(D+A)/2
print(P,Q,R,S)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_AD = line_gen(A,D)
x_CD = line_gen(C,D)
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RS = line_gen(R,S)
x_SP = line_gen(S,P)
x_BD = line_gen(B,D)
x_AC = line_gen(A,C)
#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RS[0,:],x_RS[1,:],label='$RS$')
plt.plot(x_SP[0,:],x_SP[1,:],label='$SP$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(0,-3)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(-5,0)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(0,3)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D(5,0)')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P(-2.5,-1.5)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.03), Q[1] * (1 - 0.1) , 'Q(-2.5,1.5)')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R(2.5,1.5)')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S(2.5,-1.5)')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../../figs/quad/rhombus.pdf')
plt.savefig('../../figs/quad/rhombus.eps')
#subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sss.pdf"))
#else
plt.show()







