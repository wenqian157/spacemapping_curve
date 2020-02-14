import math
import Rhino.Geometry as rg

class SDF:

    X_SCALE = 5.0
    Y_SCALE = 5.0
    Z_SCALE = 5.0

    HEIGHT = 20.0

    GLOBAL_SCALE = 40.0

    def __init__(self, x_scale = None, y_scale = None, z_scale = None, height = None, global_scale = None):

        if x_scale == None:

            self.x_scale = SDF.X_SCALE

        else:

            self.x_scale = x_scale

        if y_scale == None:

            self.y_scale = SDF.Y_SCALE

        else:

            self.y_scale = y_scale

        if z_scale == None:

            self.z_scale = SDF.Z_SCALE

        else:

            self.z_scale = z_scale

        if height == None:

            self.height_scale = SDF.HEIGHT

        else:

            self.height = height

        if global_scale == None:

            self.global_scale = SDF.GLOBAL_SCALE

        else:

            self.global_scale = global_scale

    def xyz_scale(self, pt):

        x_val = pt[0] / self.x_scale
        y_val = pt[1] / self.y_scale
        z_val = (pt[2] - self.height) / self.z_scale

        return x_val, y_val, z_val



class Gyroid(SDF):

    def get_distance(self, pt):

        x, y, z = self.xyz_scale(pt)

        dis = math.cos(x) + math.cos(y) + math.cos(z)

        return dis * self.global_scale

class SchwarzP(SDF):

    def get_distance(self, pt):

        x, y, z = self.xyz_scale(pt)

        dis = math.sin(z)*math.cos(y)+math.sin(y)*math.cos(x)+math.sin(z)*math.cos(x)

        return dis * self.global_scale 

class SchwarzD(SDF):

    def get_distance(self, pt):

        x, y, z = self.xyz_scale(pt)

        dis = math.sin(z)*math.cos(y)+math.sin(y)*math.cos(x)+math.sin(z)*math.cos(x)

        return dis * self.global_scale 

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