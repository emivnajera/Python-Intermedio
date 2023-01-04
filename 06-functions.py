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

## Parámetros por defecto y múltiples returns

def find_volume(length = 1, width =1, depth =1):
    return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10, length=5, depth=2)

print(result)
print(width)
print(text)