from spacemapping_curve.quadtree import *

import rhinoscriptsyntax as rs

class BooleanData:

    def __init__(self, objects):

        self.objects = list(objects)

    @ property
    def head(self):

        return(self.objects[0])

    @ property
    def tail(self):

        if len(self.objects) > 1:

            return self.objects[1:]

        else:

            return []

class BooleanUnion(BooleanData):

    def get_distance(self, pt):

        loc_diss = []

        for loc_obj in self.objects:

            loc_diss.append(loc_obj.get_distance(pt))

        return min(loc_diss)

class BooleanDifference(BooleanData):

    def get_distance(self, pt):

        loc_diss = [self.head.get_distance(pt)]

        for loc_obj in self.tail:

            loc_diss.append(- loc_obj.get_distance(pt))

        return max(loc_diss)

class BooleanIntersection(BooleanData):

    def get_distance(self, pt):

        loc_diss = []

        for loc_obj in self.objects:

            loc_diss.append(loc_obj.get_distance(pt))

        return max(loc_diss)


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
    
    pl = rs.AddPolyline(pts_all)

    return pl