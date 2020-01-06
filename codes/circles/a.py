import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if
r1=4
r2=3
a=np.sqrt(8**2-r2**2)
c=r2
b=8
d=r1
e=np.sqrt(8**2-r1**2)
len = 50
A = np.array([0,0])
B = np.array([8,0])

#Coordinates of P & Q
p = (b**2 + a**2-c**2 )/(2*b)
q = np.sqrt(a**2-p**2)
P= np.array([p,q])
Q= np.array([p,-q])
#Coordinates of M & N
p1 = (b**2 + d**2-e**2 )/(2*b)
q1 = np.sqrt(d**2-p1**2)
M= np.array([p1,q1])
N= np.array([p1,-q1])

O=np.array([0,0])
print(P)
print(Q)
print(M)
print(N)
O1=np.array([8,0])

 
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O).T

x_circ2 = np.zeros((2,len))
x_circ2[0,:] = r2*np.cos(theta)
x_circ2[1,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + O1).T
#Generating all lines
x_AB = line_gen(A,B)
x_AP = line_gen(A,P)
x_PB = line_gen(P,B)
x_QB = line_gen(Q,B)
x_AQ = line_gen(A,Q)
x_AM = line_gen(A,M)
x_MB = line_gen(M,B)
x_AN = line_gen(A,N)
x_NB = line_gen(N,B)
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle1$')

#Plotting all line

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')
plt.plot(x_QB[0,:],x_QB[1,:],label='$QB$')
plt.plot(x_AQ[0,:],x_AQ[1,:],label='$AQ$')
plt.plot(x_AM[0,:],x_AM[1,:],label='$AM$')
plt.plot(x_AN[0,:],x_AN[1,:],label='$AN$')
plt.plot(x_MB[0,:],x_MB[1,:],label='$MB$')
plt.plot(x_NB[0,:],x_NB[1,:],label='$NB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.2), P[1] * (1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 - 0.2), M[1] * (1) , 'M')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 - 0.2), N[1] * (1) , 'N')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/circle/circumcircle.pdf')
#plt.savefig('./figs/circle/circumcircle.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()
