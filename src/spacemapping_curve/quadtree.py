from math import sqrt
from compas.geometry import Point

class Quadtree(object):
    sq2 = sqrt(2.0)
    sq3 = sqrt(3.0)

    def __init__(self):
        self._p = Point(0, 0, 0)
        self._ws = 100.0  # world size
        self._ml = 4      # max levels
        self._rn = QuadNode(0, 0, 0, self._ws, 0, 1)
        self._o = None
        self.leafs = []
    
    def divide(self, node):
        d = self._o.get_distance(node._p)
        node.distance = d
        
        if node.level < self._ml:            
            if abs(d) < Quadtree.sq2 * node._el/2.0:
                node.divide_node()     
                for b in node._branches:
                    self.divide(b)
            else:
                node.divide_node()
                self.leafs.append(node)
                    
        else:
            # if abs(node.distance) < Quadtree.sq2 * node._el/2.0:
            node.divide_node()
            self.leafs.append(node)


class QuadNode(object):
    def __init__(self, x, y, z, e, l, orientation):
        self._p = Point(x, y, z)
        self._el = e
        self._l = l
        self._branches = None
        self.distance = 0.0
        self.orientation = orientation
    
    @property
    def level(self):
        return self._l

    @level.setter
    def level(self, l):
        self._l = float(l)
    
    def divide_node(self):
        self._branches = []
        qs = self._el/4.0
        nl = self.level + 1

        if self.orientation == 1:
            self._branches.append(QuadNode(self._p.x-qs, self._p.y-qs, 0, qs*2, nl, (self.orientation-1)%4))
            self._branches.append(QuadNode(self._p.x-qs, self._p.y+qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x+qs, self._p.y+qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x+qs, self._p.y-qs, 0, qs*2, nl, (self.orientation+1)%4))

        elif self.orientation == 0:
            self._branches.append(QuadNode(self._p.x-qs, self._p.y-qs, 0, qs*2, nl, (self.orientation+1)%4))
            self._branches.append(QuadNode(self._p.x+qs, self._p.y-qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x+qs, self._p.y+qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x-qs, self._p.y+qs, 0, qs*2, nl, (self.orientation-1)%4))

        elif self.orientation == 2:
            self._branches.append(QuadNode(self._p.x+qs, self._p.y+qs, 0, qs*2, nl, (self.orientation+1)%4))
            self._branches.append(QuadNode(self._p.x-qs, self._p.y+qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x-qs, self._p.y-qs, 0, qs*2, nl, self.orientation%4))           
            self._branches.append(QuadNode(self._p.x+qs, self._p.y-qs, 0, qs*2, nl, (self.orientation-1)%4))

        elif self.orientation == 3:
            self._branches.append(QuadNode(self._p.x+qs, self._p.y+qs, 0, qs*2, nl, (self.orientation-1)%4))
            self._branches.append(QuadNode(self._p.x+qs, self._p.y-qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x-qs, self._p.y-qs, 0, qs*2, nl, self.orientation%4))
            self._branches.append(QuadNode(self._p.x-qs, self._p.y+qs, 0, qs*2, nl, (self.orientation+1)%4))


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":
    pass
