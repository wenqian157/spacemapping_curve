import rhinoscriptsyntax as rs 
import scriptcontext as sc
from Rhino.Geometry import Point3d
from System.Drawing.Color import FromArgb
from Rhino.DocObjects.ObjectColorSource import ColorFromObject

find_object = sc.doc.Objects.Find
add_point = sc.doc.Objects.AddPoint
find_layer_by_fullpath = sc.doc.Layers.FindByFullPath


def square(matrix, a, b):
    pts = []
    for x in range(-int(matrix[0]/2), int(matrix[0]/2)):
        for y in range(-int(matrix[1]/2), int(matrix[1]/2)):
            d = abs(max(abs(x)-a/2, abs(y)-b/2))
            pts.append({'pos':(x, y, 0), 'color': d})

    return pts

def circle(r):
    pass

def remap(x, in_domain, out_domain):
    return (x - in_domain[0]) * (out_domain[1] - out_domain[0]) / (in_domain[1] - in_domain[0]) + out_domain[0]

def show(pts):
    if rs.IsLayer('Points'):
        rs.PurgeLayer('Points')

    colors = [pt['color'] for pt in pts]
    d_max = sorted(colors)[-1]
    for pt in pts:
        color = remap(pt['color'], (0, d_max), (0, 255))

        rs.AddLayer('Points')
        pos = pt['pos']
        guid = add_point(Point3d(*pos))
        obj = find_object(guid)
        attr = obj.Attributes
        attr.ObjectColor = FromArgb(color, color, color)
        attr.ColorSource = ColorFromObject
        index = find_layer_by_fullpath('Points', True)
        if index >= 0:
            attr.LayerIndex = index
        obj.CommitChanges()


if __name__ == '__main__':
    matrix = (100, 100)
    pts = square(matrix, 10, 90)
    show(pts)

