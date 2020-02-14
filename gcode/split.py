txt = """G1 X95.096 Y73.561 E0.2361
G1 X95.397 Y73.228 E0.3108
G1 X96.725 Y71.903 E0.6228"""

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

