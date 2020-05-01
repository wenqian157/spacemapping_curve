from compas.geometry import Cylinder
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Circle
from compas.geometry import Sphere
from compas.geometry import Plane

from compas_vol.meshing import *
from compas_vol.primitives import *
from compas_vol.combinations import *

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

from spacemapping_curve.hilbertcurve import draw_hc
from spacemapping_curve.hilbertcurve import draw_hc_b
from spacemapping_curve.TSP import *


frame = Frame([0, 0, 0], [1, 0, 0], [0, 1, 0])
# box = Box(Frame.worldXY(), 150, 90, 200)
box = Box(frame, 150, 90, 200)
volbox = VolBox(box)

plane = Plane([0, 0, 0], [0, 0, 1])
circle = Circle(plane, 50)
cylinder = Cylinder(circle, 90)
volcylinder = VolCylinder(cylinder)

sphere = Sphere((40, 20, 0), 50)
volshpere = VolSphere(sphere)

sphere_big = Sphere((40, 20, 0), 100)
volshpere_big = VolSphere(sphere_big)

union = Union(volbox, volshpere)
substract = Subtraction(volshpere_big, volshpere)

dist = substract

# draw_hc(200, 7, dist)
# draw_hc_b(200, 7, dist)


# pts = draw_hc_b(200, 7, dist)
pts = draw_hc_b(200, 7, dist, return_pts=True)
print(len(pts))
route = get_TSP_greedy(pts)
route = pairwise_exchange(pts, route, 8000000)
rs.AddPolyline([pts[i] for i in route])
