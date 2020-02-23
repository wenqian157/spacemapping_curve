from spacemapping_curve.quadtree import *
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

def draw_hc(ws, ml, function, return_pts = False):
    tree = Quadtree()
    tree._ws = ws
    tree._ml = ml
    tree._o = function
    tree._rn = QuadNode(0, 0, 50, ws, 0, 1)
    tree.divide(tree._rn)
    pts = []

    for node in tree.leafs:
        pt = node._p
        pts.append(pt)
    
    if not(return_pts):
        pl = rs.AddPolyline(pts)

    else:
        pl = [rg.Point3d(pt[0], pt[1], pt[2]) for pt in pts]

    return pl