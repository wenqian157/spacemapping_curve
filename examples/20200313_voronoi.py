# import numpy
# import scipy
# from compas.rpc import Proxy
# cg = Proxy('compas.geometry')
# voronoi = cg.voronoi_from_points_numpy
# from compas.geometry.triangulation import voronoi_from_points_numpy
# from compas.geometry import voronoi_from_points_numpy

# import compas_rhino

# guids = compas_rhino.select_points()
# points = compas_rhino.get_point_coordinates(guids)
# voronoi = voronoi(points)
# print(points)


import json
import os
filepath = 'points.json'
# with open(filepath, 'w') as f:
#     json.dump(points, f, indent=4)

HERE = os.path.dirname(__file__)
FILE = os.path.join(HERE, filepath)
print(FILE)
with open(FILE, 'r') as f:
    points = json.load(f)

# print(points)
# voronoi = voronoi_from_points_numpy(points)

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter
from compas.geometry import closest_point_on_line_xy
from compas.geometry import voronoi_from_points_numpy

mesh = Mesh()

points = [[pt[0], pt[1]] for pt in points]
for pt in points:
    mesh.add_vertex(x=pt[0], y=pt[1])
# mesh.add_vertex(x=0, y=0)
# mesh.add_vertex(x=1.5, y=0)
# mesh.add_vertex(x=1, y=1)
# mesh.add_vertex(x=0, y=2)

# mesh.add_face([0, 1, 2, 3])

sites = mesh.vertices_attributes('xy')

sites = points
voronoi = voronoi_from_points_numpy(sites)
# print(voronoi.ridge_vertices)
# print(voronoi.ridge_points)
points = []
for xy in voronoi.vertices:
    points.append({
        'pos'       : xy,
        'radius'    : 0.02,
        'facecolor' : '#ff0000',
        'edgecolor' : '#ffffff',
    })

lines = []
arrows = []
for (a, b), (c, d) in zip(voronoi.ridge_vertices, voronoi.ridge_points):
    if a > -1 and b > -1:
        lines.append({
            'start' : voronoi.vertices[a],
            'end'   : voronoi.vertices[b],
            'width' : 1.0,
            'color' : '#ff0000',
        })
    elif a == -1:
        sp = voronoi.vertices[b]
        ep = closest_point_on_line_xy(sp, (voronoi.points[c], voronoi.points[d]))
        arrows.append({
            'start' : sp,
            'end'   : ep,
            'width' : 1.0,
            'color' : '#00ff00',
            'arrow' : 'end'
        })
    else:
        sp = voronoi.vertices[a]
        ep = closest_point_on_line_xy(sp, (voronoi.points[c], voronoi.points[d]))
        arrows.append({
            'start' : sp,
            'end'   : ep,
            'width' : 1.0,
            'color' : '#00ff00',
            'arrow' : 'end'
        })
# print(voronoi.ridge_vertices)
# print(voronoi.ridge_points)
print(voronoi.point_region[3])
print(voronoi.regions[voronoi.point_region[3]])
print([voronoi.vertices[key] for key in voronoi.regions[voronoi.point_region[3]]])
# print(voronoi.point_region[0])

plotter = MeshPlotter(mesh)
plotter.draw_points(points)
plotter.draw_lines(lines)
plotter.draw_arrows(arrows)
plotter.draw_vertices(radius=0.02)
plotter.draw_faces()
plotter.show()

# print(points)
# print(lines)
# print(arrows)


