import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if


len = 50
O1=np.array([0,0])
r1=2
O2=np.array([3,0])
r2=2
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O1).T
a=2
b=2
c=3
p = (c**2 + b**2-a**2 )/(2*c)
q = np.sqrt(b**2-p**2)
B = np.array([p,q])
C = np.array([p,-q])
A = np.array([-2,0]) 
Q = np.array([5,0])
m=A-B
d=np.linalg.norm(m)
s=2*m.T*C

x=-(s/d**2)

P=B+x*m
m1=Q-B
d1=np.linalg.norm(m)
s1=2*m1.T*B

x1=(s1/d1**2)

D=B+x1*m1
print(A,B,C,D,P,Q)
x_circ2 = np.zeros((2,len))
x_circ2[0,:] = r2*np.cos(theta)
x_circ2[1,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + O2).T
#Generating all lines
x_AP = line_gen(A,P)
x_PB = line_gen(P,B)
x_BQ = line_gen(B,Q)
x_QC = line_gen(Q,C)
x_CP = line_gen(C,P)
x_AB = line_gen(A,B)
x_BD = line_gen(B,D)
x_DC = line_gen(D,C)
x_CA = line_gen(C,A)
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle1$')

#Plotting all line
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')
plt.plot(x_BQ[0,:],x_BQ[1,:],label='$BQ$')
plt.plot(x_QC[0,:],x_QC[1,:],label='$QC$')
plt.plot(x_CP[0,:],x_CP[1,:],label='$CP$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_DC[0,:],x_DC[1,:],label='$DC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(-2,0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(1.5,1.32)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(1.5,-1.32)')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D(4.125,1.65)')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P(-1.125,1.65)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.03), Q[1] * (1 - 0.1) , 'Q(5,0)')
plt.plot(O1[0], O1[1], 'o')
plt.text(O1[0] * (1 + 0.03), O1[1] * (1 - 0.1) , 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../../figs/circles/3.pdf')
plt.savefig('../../figs/circles/3.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()
