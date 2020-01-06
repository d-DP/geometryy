#Code by P.Durga Prasad
#December 31, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import *


#if using termux
#import subprocess
#import shlex
#end if


#Triangle sides
#a = 6
#b = 4.5
#c = 7.5
a = 3.5
b = 6.5
angD = (np.pi/180)*105
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angD))
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
ang=math.radians(60)
M=np.array([0,0])
I=np.array([a,0])
S=np.array([p,q])
print(S)
an=np.tan((np.pi/180)*135)
#direction vector of ST
m1=np.array([1,an])
#normal vector of ST
n1 = np.matmul(omat,m1)
#print(n1)
#Direction vector of ST = MT
m2=S-I
#normal vector of MT
n2 = np.matmul(omat,m2)
#print(n2)
#T = line_intersect(n1,S,n2,M)
N=np.vstack((n1,n2))
#print(n1,n2,N)
r = np.zeros(2)
r[0] = n1@S
r[1] = n2@M
#print(r)
#Intersection
T=np.linalg.inv(N)@r
print(T)

#Generating all lines
x_MI = line_gen(M,I)
x_IS = line_gen(I,S)
x_MS = line_gen(M,S)
x_ST = line_gen(S,T)
x_MT = line_gen(M,T)
#Plotting all lines
plt.plot(x_MI[0,:],x_MI[1,:],label='$MI$')
plt.plot(x_IS[0,:],x_IS[1,:],label='$IS$')
plt.plot(x_MS[0,:],x_MS[1,:],label='$MS$')
plt.plot(x_ST[0,:],x_ST[1,:],label='$ST$')
plt.plot(x_MT[0,:],x_MT[1,:],label='$MT$')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.1), M[1] * (1 - 0.1) , 'M(0,0)')
plt.plot(I[0], I[1], 'o')
plt.text(I[0] * (1 +0.1), I[1] * (1) , 'I(3.5,0)')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S(5.18,6.27)')
plt.plot(T[0], T[1], 'o')
plt.text(T[0] * (1 + 0.03), T[1] * (1 - 0.1) , 'T(2.42,9.03)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('../../figs/quad/quad_constr.pdf')
plt.savefig('../../figs/quad/quad_constr.eps')
#subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sss.pdf"))
#else
plt.show()







