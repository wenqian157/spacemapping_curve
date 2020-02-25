from spacemapping_curve.quadtree import *
from spacemapping_curve.distance import Gyroid
from spacemapping_curve.distance import DistanceToCurve
from spacemapping_curve.hilbertcurve import draw_hc
from spacemapping_curve.combinations import *
from spacemapping_curve.TSP import get_TSP_greedy

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs 

# ==============================================================================
# get distance value
# ==============================================================================
guid = rs.GetObject("select curves", filter=rs.filter.curve)
crv_1 = rs.coercecurve(guid)

guid = rs.GetObject("select curves", filter=rs.filter.curve)
crv_2 = rs.coercecurve(guid)

crv_distance1 = DistanceToCurve([crv_2])
crv_distance2 = DistanceToCurve([crv_1])

crv_distance = BooleanUnion([crv_distance1, crv_distance2])
crv_distance = BooleanDifference([crv_distance1, crv_distance2])

# ==============================================================================
# Main
# ==============================================================================

pts = draw_hc(200, 7, crv_distance1, return_pts=True)
print(len(pts))
route = get_TSP_greedy(pts)
rs.AddPolyline([pts[i] for i in route])

# rs.AddPoints(pts)