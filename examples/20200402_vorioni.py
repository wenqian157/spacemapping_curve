import Rhino.Geometry as rg
import math

dots = []

i = 0
r = 0

while i < 2000 and r < stop_r:

    r = spacing * math.sqrt(i) * (scale_factor ** (i / scale_step) ) * scale_start_factor
    theta = i * 2.4 + start_angle
    
    pt = rg.Point3d(
        x = b_pt[0] + math.cos(theta) * r,
        y = b_pt[1] + math.sin(theta) * r,
        z = 0
    )

    i+=1

    dots.append(pt)
    
i = 1
r = 0
while i < 2000 and r < stop_r:

    r = spacing * math.sqrt(i) * (scale_factor ** (i / scale_step) ) * scale_start_factor
    theta = i * 2.4 + start_angle
    
    pt = rg.Point3d(
        x = b_pt[0] + math.cos(theta) * r,
        y = b_pt[1] + math.sin(theta) * r,
        z = 0
    )

    i+=1

    dots.append(pt)