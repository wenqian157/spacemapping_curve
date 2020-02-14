import Rhino.Geometry as rg
import math

global z_height, scale_val, max_depth, side_length

def depthFunction(x, y, x_count, y_count):
       
    ## Gyroid
    px = x / scale_val
    py = y / scale_val
    pz = (z_height / side_length) / scale_val
    
    val = math.sin(px)*math.cos(py) + math.sin(py)*math.cos(pz) + math.sin(pz)*math.cos(px)
    
    depth = int((2 + val) * (max_depth) / 4)
    
    ## DistanceToDot
    
    # d_x = x - x_count * .5
    # d_y = y - y_count * .5
    # d_z = z_height / side_length - x_count * .5
    
    # depth = max_depth - math.sqrt(d_x ** 2 + d_y **2 + d_z ** 2) * scale_val
    # depth = int(depth)
    
    if depth < 1:
        
        depth = 1
        
    elif depth > max_depth:
        
        depth = max_depth
    
    return depth

def cellGrid(x_count, y_count, side_length = 10.0, depth = 4,spacing = .5):

    x_count = int(x_count / 2) * 2 + 1

    pt_list = []

    for j in range(y_count):

        line_val = 2 * (j % 2)
        start_x_index = (x_count - 1) * (j % 2)

        for i in range(x_count):
            
            print(abs(start_x_index - i), j)
            
            depth_val = depthFunction(abs(start_x_index - i) + j % 2, j, x_count, y_count)
            print("depth: ", depth_val)

            pt_list.extend(simpleCell(
                cell_type=line_val + i % 2,
                depth = depth_val,
                cell_index = (abs(start_x_index - i), j),
                spacing = spacing,
                side_length = side_length
            ))

    return pt_list


def simpleCell(cell_type = 0, spacing = 1.0, depth = 2, side_length = 10.0, cell_index = (0,0)):

    base_x_0 = cell_index[0] * side_length + spacing
    base_x_1 = (cell_index[0] + 1) * side_length - spacing

    base_y_0 = cell_index[1] * side_length + spacing
    base_y_1 = (cell_index[1] + 1) * side_length - spacing

    y_step = (side_length - spacing * 2.0) / 2.0 ** depth

    if cell_type == 0:

        # A form, going from bottom left to top right
        x0, x1 = base_x_0, base_x_1
        y0 = base_y_0

        y_direction = 1.0

    elif cell_type == 1:

        # B form, going from top left to bottom right

        x0, x1 = base_x_0, base_x_1
        y0 = base_y_1

        y_direction = -1.0

    elif cell_type == 2:

        # C form, going from top right to bottom left
        x0, x1 = base_x_1, base_x_0
        y0 = base_y_1

        y_direction = -1.0

    elif cell_type == 3:

        # D form, going from bottom right to top left
        x0, x1 = base_x_1, base_x_0
        y0 = base_y_0

        y_direction = 1

    pt_list = []

    for i in range(0, 2 ** depth + 1, 1):

        y_val = y0 + i * y_direction * y_step

        if i % 2 == 0:

            pt_list.extend([
                rg.Point3d(x0, y_val, z_height), 
                rg.Point3d(x1, y_val, z_height)
            ])

        else:

            pt_list.extend([
                    rg.Point3d(x1, y_val, z_height), 
                    rg.Point3d(x0, y_val, z_height)
                ])

    return pt_list

if depth > max_depth:
    
    depth = max_depth

side_length = spacing * (2 ** max_depth)

a = cellGrid(x, y, depth = depth, spacing = spacing, side_length = side_length)
