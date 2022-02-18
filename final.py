def polyFit(x, y):
    import numpy as np
    xx = np.array(x)
    yy = np.array(y)

    z1 = np.polyfit(xx, yy, 1)
    p1 = np.poly1d(z1)
    yx1 = [p1(i) for i in xx]

    z2 = np.polyfit(xx, yy, 2)
    p2 = np.poly1d(z2)
    yx2 = [p2(i) for i in xx]

    z3 = np.polyfit(xx, yy, 3)
    p3 = np.poly1d(z3)
    yx3 = [p3(i) for i in xx]

    from matplotlib import pylab
    figure, axis = pylab.subplots(2, 2)
    pylab.xlabel('x')
    pylab.ylabel('y')
    figure.suptitle('Polynomial Fitting Graphs', fontsize=16)

    axis[0, 0].plot(xx, yy, 'ro')
    axis[0, 0].set_title('Original Data')

    axis[0, 1].plot(xx, yy, 'ro')
    axis[0, 1].plot(xx, yx1, 'k')
    axis[0, 1].set_title('Best-Fit Line')

    axis[1, 0].plot(xx, yy, 'ro')
    axis[1, 0].plot(xx, yx2, 'k')
    axis[1, 0].set_title('Best-Fit 2nd Order Polynomial')

    axis[1, 1].plot(xx, yy, 'ro')
    axis[1, 1].plot(xx, yx3, 'k')
    axis[1, 1].set_title('Best-Fit 3rd Order Polynomial')

    pylab.tight_layout()
    figure.subplots_adjust(top=0.88)
    pylab.savefig('Polynomial Fitting.pdf')
    pylab.show()


x = [107.608, 108.632, 109.773, 110.929, 112.075, 113.270, 115.094, 116.219,
     117.388, 118.734, 120.445, 121.950, 123.366, 125.368, 127.852, 130.081]
y = [60.323, 61.122, 60.171, 61.187, 63.221, 63.639, 64.989, 63.761, 66.019,
     67.857, 68.169, 66.513, 68.655, 69.564, 69.331, 70.551]

polyFit(x, y)
