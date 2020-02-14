import math
import Rhino.Geometry as rg

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