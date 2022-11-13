def digital_root(n):
    value = 0
    nlist = [int(i) for i in str(n)]
    for i in nlist:
        value += i
    if value >= 10:
        return digital_root(value)
    else:
        return value

print(digital_root(493193))