from spacemapping_curve.quadtree import *
from spacemapping_curve.distance import Gyroid
from spacemapping_curve.distance import DistanceToCurve
from spacemapping_curve.hilbertcurve import draw_hc
from spacemapping_curve.hilbertcurve import draw_hc_b
from spacemapping_curve.combinations import *
from spacemapping_curve.TSP import *

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs 

# ==============================================================================
# get distance value
# ==============================================================================

crvs = []
guids = rs.GetObjects("select curves", filter=rs.filter.curve)
for guid in guids:
    crv = rs.coercecurve(guid)
    crvs.append(crv)

print(crvs)
crv_distance = DistanceToCurve(crvs)

# crv_distance = BooleanUnion([crv_distance1, crv_distance2])

# ==============================================================================
# Main
# ==============================================================================

pts = draw_hc(110, 7, crv_distance)
