from spacemapping_curve.quadtree import *
from spacemapping_curve.distance import FuckYouBernhardFunction
from spacemapping_curve.distance import DistanceToCurve
from spacemapping_curve.hilbertcurve import draw_hc

import Rhino.Geometry as rg


pts_1 = [
    rg.Point3d(-100, 0, 0),
    rg.Point3d(-50, 50, 0),
    rg.Point3d(50, -50, 0),
    rg.Point3d(100, 50, 0),
    rg.Point3d(150, 150, 0)
]

pts_2 = [
    rg.Point3d(100, 0, 0),
    rg.Point3d(50, 50, 0),
    rg.Point3d(-50, -50, 0),
    rg.Point3d(100, 50, 0),
    rg.Point3d(0, 150, 0)
]

crv_1 = rg.NurbsCurve.CreateControlPointCurve(pts_1)
crv_2 = rg.NurbsCurve.CreateControlPointCurve(pts_2)

crv_distance = DistanceToCurve([crv_1, crv_2])
# gyroid = FuckYouBernhardFunction()

draw_hc(200, 10, crv_distance)