def likes(names):
    type = False
    if len(names) == 0:
        prefix = "no one"
        type = True
    elif len(names) == 1:
        prefix = str(names[0])
        type = True
    elif len(names) == 2:
        prefix = f"{names[0]} and {names[1]}"
    elif len(names) == 3:
        prefix = f"{names[0]}, {names[1]} and {names[2]}"
    else:
        prefix = f"{names[0]}, {names[1]} and {len(names) - 2} others"
    if type == False:
        sentence = f"{prefix} like this"
    else:
        sentence = f"{prefix} likes this"
    return sentence

print(likes(['Alex', 'Jacob', 'Mark', 'Max']))