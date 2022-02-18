from matplotlib import pylab
import numpy as N

x = N.arange(-3.14, 3.14, 0.01)
y = N.sin(x)
pylab.plot(x, y, label='sin(x)')
pylab.savefig('myplot.png')  # saves png file
pylab.savefig('myplot.eps')  # saves eps file
pylab.savefig('myplot.pdf')  # saves pdf file
