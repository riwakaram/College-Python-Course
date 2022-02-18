import math
import vpython as vp

ball = vp.sphere()
box = vp.box(pos=vp.vector(0, -1, 0), width=4, length=4, height=0.5)
# tell visual not to automatically scale the image
vp.scene.autoscale = False
for i in range(1000):
    t = i * 0.1
    y = math.sin(t)
    # update the ball’s position
    ball.pos = vp.vector(0, y, 0)
    # ensure we have only 24 frames per second
    vp.rate(24)
