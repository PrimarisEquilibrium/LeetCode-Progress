def move_zeros(array):
    zero_list = []
    rest = []
    for i in array:
        if i == 0:
            zero_list.append(i)
        else:
            rest.append(i)
    return rest + zero_list

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
