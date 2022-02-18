import vpython as vp

sphere1 = vp.sphere(pos=vp.vector(0, 0, 0), color=vp.vector(0, 0, 1))
sphere2 = vp.sphere(pos=vp.vector(5, 0, 0), color=vp.vector(1, 0, 0), radius=2)
base = vp.box(pos=vp.vector(0, -2, 0), length=8, height=0.1, width=10)
