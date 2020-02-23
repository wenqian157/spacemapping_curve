from spacemapping_curve.quadtree import *

tree = Quadtree()
node = QuadNode(0, 0, 0, 100, 0, 1)
node.divide_node()
for b in node._branches:
    tree.leafs.append(b)
tree.leafs.append(node)
print(tree.leafs)