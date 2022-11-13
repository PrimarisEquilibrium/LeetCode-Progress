def minimum(arr):
    v = arr[0]
    for i in arr:
        if i < v:
            v = i
    return v
        

def maximum(arr):
    v = arr[0]
    for i in arr:
        if i > v:
            v = i
    return v