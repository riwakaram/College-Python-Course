def bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0,
                     mux=0.0, muy=0.0, sigmaxy=0.0):
    """Bivariate Gaussian distribution for equal shape *X*, *Y*.
    See `bivariate normal
    <https://mathworld.wolfram.com/BivariateNormalDistribution.html>`_
    at mathworld.
    """
    Xmu = X - mux
    Ymu = Y - muy

    rho = sigmaxy / (sigmax * sigmay)
    z = Xmu ** 2 / sigmax ** 2 + Ymu ** 2 / sigmay ** 2 - 2 * rho * Xmu * Ymu / (sigmax * sigmay)
    denom = 2 * np.pi * sigmax * sigmay * np.sqrt(1 - rho ** 2)
    return np.exp(-z / (2 * (1 - rho ** 2))) / denom


import numpy as np
import matplotlib.mlab as mlab  # Matlab compatibility commands
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # Colour map submodule

# create matrix Z that contains some data interesting data
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = bivariate_normal(X, Y, 3.0, 1.0, 0.0, 0.0)
Nx, Ny = 2, 3
plt.subplot(Nx, Ny, 1)
# next plot will be shown in
# first subplot in Nx x Ny
# matrix of subplots
plt.imshow(Z, cmap=cm.jet)  # default colourmap ’jet’
plt.title("colourmap jet")
plt.subplot(Nx, Ny, 2)  # next plot for second subplot
plt.imshow(Z, cmap=cm.jet_r)  # reverse colours in jet
plt.title("colourmap jet_r")
plt.subplot(Nx, Ny, 3)
plt.imshow(Z, cmap=cm.gray)
plt.title("colourmap gray")
plt.subplot(Nx, Ny, 4)
plt.imshow(Z, cmap=cm.hsv)
plt.title("colourmap hsv")
plt.subplot(Nx, Ny, 5)
plt.imshow(Z, cmap=cm.gist_earth)
plt.title("colourmap gist_earth")
plt.subplot(Nx, Ny, 6)
# make isolines by reducing number of colours to 10
mycmap = cm.get_cmap('jet', 10)  # 10 discrete colors
plt.imshow(Z, cmap=mycmap)
plt.title("colourmap jet\n(10 colours only)")
plt.savefig("pylabimshowcm.pdf")
plt.show()
