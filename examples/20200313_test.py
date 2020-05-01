import compas_rhino

guids = compas_rhino.select_points()
points = compas_rhino.get_point_coordinates(guids)

import json
import os
filepath = 'points.json'
with open(filepath, 'w') as f:
    json.dump(points, f, indent=4)