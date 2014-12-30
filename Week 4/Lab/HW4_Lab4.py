
#############################
####     Performance     ####
#############################

def insertionsort(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                (A[i], A[j]) = (A[j], A[i])


B =  []
import random
for i in range(0,10000):
    B.append(random.random())

Bsorted = sorted(B)
insertionsort(B)
assert B == Bsorted

%timeit [insertionsort(B)]
%timeit [sorted(B)]


# 100 ms - Insertion Sort
insrt100 =  []

for i in range(0,912):
    insrt100.append(random.random())
    
%timeit [insertionsort(insrt100)]


# 1 s - Insertion Sort
insrt1 =  []

for i in range(0,2750):
    insrt1.append(random.random())

%timeit [insertionsort(insrt1)]


# 10 s - Insertion Sort
insrt10 =  []

for i in range(0,8000):
    insrt10.append(random.random())

%timeit [insertionsort(insrt10)]


# 100 ms - Built in Sort
srt100 =  []

for i in range(0,77000):
    srt100.append(random.random())
    
%timeit [sorted(srt100)]


# 1 s - Built in Sort
srt1 =  []

for i in range(0,600000):
    srt1.append(random.random())

%timeit [sorted(srt1)]


# 10 s - Built in Sort
srt10 =  []

for i in range(0,4500000):
    srt10.append(random.random())

%timeit [sorted(srt10)]

#############################
####      Graphing       ####
#############################

from numpy import *
from pylab import *
iterations = 1000

density = 1000
x_min, x_max = -1, 2
y_min, y_max = -1.5, 1.5
x, y = meshgrid(linspace(x_min, x_max, density),
linspace(y_min, y_max, density))

c = x + 1j*y
z = c.copy()
m = zeros((density, density))
for n in xrange(iterations):
    print "Iteration No." , n
    indices = (abs(z) <= 1)
    z[indices] = z[indices]**2 + c[indices] 
    m[indices] = n
imshow(m,
extent=(x_min, x_max, y_min, y_max))
title('Mandelbrot Set')
xlabel('Re(z)')
ylabel('Im(z)')
show()
