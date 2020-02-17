from spacemapping_curve.quadtree import *
import rhinoscriptsyntax as rs

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