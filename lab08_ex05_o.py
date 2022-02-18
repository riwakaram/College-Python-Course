import vpython as vp
import math

ball1 = vp.sphere(pos=vp.vector(0, 0, 0), radius=2)
ball2 = vp.sphere(pos=vp.vector(5, 0, 0), radius=2)
connection = vp.cylinder(pos=ball1.pos, axis=ball2.pos - ball1.pos)
for t in range(100):
    # move ball2
    ball2.pos = (-t, math.sin(t), math.cos(t))
    # keep cylinder connection between ball1 and ball2
    connection.axis = ball2.pos - ball1.pos
    vp.rate(24)
