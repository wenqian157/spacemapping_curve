from compas.geometry import Cylinder
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Circle
from compas.geometry import Sphere
from compas.geometry import Plane

from compas_vol.meshing import *
from compas_vol.primitives import *
import compas_vol.microstructures as cvm
from compas_vol.combinations import *

from compas_rhino.artists import PointArtist
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

import math

frame = Frame([10, 0, 0], [1, 0, 0], [0, 1, 0])
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


class FuckYouBernhardFunction:

    X_SCALE = 5.0
    Y_SCALE = 5.0
    Z_SCALE = 5.0

    HEIGHT = 20.0

    GLOBAL_SCALE = 40.0

    def __init__(self):

        pass

    def get_distance(self, pt):

        x_val = pt[0] / FuckYouBernhardFunction.X_SCALE
        y_val = pt[1] / FuckYouBernhardFunction.Y_SCALE
        z_val = (pt[2] - FuckYouBernhardFunction.HEIGHT) / FuckYouBernhardFunction.Z_SCALE

        dis = math.sin(x_val)*math.cos(y_val)+math.sin(y_val)*math.cos(x_val)+math.sin(z_val)*math.cos(x_val)

        return dis * FuckYouBernhardFunction.GLOBAL_SCALE

class DistanceToCurve:

    GLOBAL_SCALE = 1.0

    def __init__(self, crvs):

        if not(isinstance(crvs, list)):

            self.crvs = [crvs]

        else:

            self.crvs = crvs

    def get_distance(self, pt):
        
        other_pt = rg.Point3d(pt[0], pt[1], pt[2])

        distance_list = []

        for crv in self.crvs:

            pt_on_crv = crv.PointAt(crv.ClosestPoint(other_pt)[1])

            distance = pt_on_crv.DistanceTo(other_pt) / DistanceToCurve.GLOBAL_SCALE

            distance_list.append(distance)

        distance_list.sort()

        return distance_list[0]

# defining some points

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
gyroid = FuckYouBernhardFunction()

def draw_hc(ws, ml, function):
    tree = Quadtree()
    tree._ws = ws
    tree._ml = ml
    tree._o = function
    tree._rn = QuadNode(0, 0, 50, ws, 0, 1)
    tree.divide(tree._rn)
    pts_all = []

    for node in tree.leafs:
        # artist = PointArtist(node._p)
        # artist.draw()
        pts = [b._p for b in node._branches]
        pts_all.extend(pts)
    rs.AddPolyline(pts_all)

draw_hc(200, 10, gyroid)