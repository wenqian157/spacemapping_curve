from spacemapping_curve.quadtree import *
from spacemapping_curve.distance import FuckYouBernhardFunction
from spacemapping_curve.distance import DistanceToCurve
from spacemapping_curve.hilbertcurve import draw_hc

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs 

# ==============================================================================
# get distance value
# ==============================================================================
guid = rs.GetObject("select curves", filter=rs.filter.curve)
crv_1 = rs.coercecurve(guid)

guid = rs.GetObject("select curves", filter=rs.filter.curve)
crv_2 = rs.coercecurve(guid)

crv_distance = DistanceToCurve([crv_1, crv_2])
crv_distance = DistanceToCurve([crv_1])

# ==============================================================================
# Main
# ==============================================================================

draw_hc(200, 7, crv_distance)
