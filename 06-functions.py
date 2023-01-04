def suma (a,b):
    print(a+b)

suma(5,4)


##return

def suma2(min, max):
    sum = 0
    for x in range(min,max):
        sum += x
    return sum

print(suma2(1,10))