from scipy import *
from pylab import *

t = arange(0,1,0.1)
y = t**2

figure(1)
clf()
plot(t,y)

xlabel('Time (sec)')
ylabel('y')
title('a basic plot')

show()
