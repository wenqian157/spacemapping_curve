from spacemapping_curve.quadtree import *
import spacemapping_curve.distance as sdf
import spacemapping_curve.hilbertcurve as hc

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs 

# ==============================================================================
# get distance value
# ==============================================================================
GLOBAL_SCALE = 10
x = 10
y = 10
z = 10
height = 20
max_depth = 7

sdf.DistanceToCurve.GLOBAL_SCALE = GLOBAL_SCALE

# crv_distance = sdf.DistanceToCurve(crvs)
crv_distance = sdf.Gyroid(x, y, z, height, GLOBAL_SCALE)

# ==============================================================================
# Main
# ==============================================================================

a = hc.draw_hc(200, max_depth, crv_distance)
b = hc.draw_hc_b(200, max_depth-1, crv_distance)
