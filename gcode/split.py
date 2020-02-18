txt = """G1 F480 X96.117 Y72.633 E0.1089
G1 X97.517 Y71.450 E0.4137
G1 X97.953 Y71.156 E0.5012
G1 X98.286 Y70.977 E0.5640
G1 X98.969 Y70.656 E0.6895
G1 X99.497 Y70.273 E0.7980
G1 X99.713 Y70.080 E0.8462"""

txt_list = txt.split('\n')
txt_lists = [txt.split(' ') for txt in txt_list]

txt_lists = [[float(txt[1:]) for txt in txt_list[1:]] for txt_list in txt_lists]

print(txt_lists)

x, y, e = list(zip(*(txt_lists)))

count = len(x)

distances = []

for i in range(count - 1):

    distance = ((x[i] - x[i + 1]) ** 2 + (y[i] - y[i + 1]) ** 2) ** .5

    print(distance, e[i])
    print(distance, e[i + 1])

    print ( (e[i + 1] - e[i]) / distance)

