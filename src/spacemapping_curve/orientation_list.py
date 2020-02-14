# orientation list

a = [ 
    [ [-1, 1, 1, -1], [-1, -1, 1, 1] ],
    [ [-1, -1, 1, 1], [-1, 1, 1, -1] ],
    [ [1, -1, -1, 1], [1, 1, -1, -1] ],
    [ [1, 1, -1, -1], [1, -1, -1, 1] ]
]

trial_list = []

base_list = [-1, -1, 1, 1]

index_tuple_list = [(1, 0), (0, 1), (3, 2), (2, 3)]

for i in range(4):

    i_a, i_b = index_tuple_list[i]

    loc_list_a = [base_list[(j + i_a) % 4] for j in range(4)]
    loc_list_b = [base_list[(j + i_b) % 4] for j in range(4)]

    trial_list.append([loc_list_a, loc_list_b])

print(a)
print(trial_list)