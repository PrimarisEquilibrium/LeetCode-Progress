first = True
def persistence(n):
    global first
    if n < 10 and first == True:
        return 0
    first = False
           
    n = [int(i) for i in str(n)]
    value = 1
    for i in n:
        i = i * value
        value = i
    if value >= 10:
        return persistence(value)
    else:
        return value
    
print(persistence(4))