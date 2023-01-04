numbers = []

for element in range (1,11):
    numbers.append(element)

print(numbers)

numbers2 = [element for element in range(1,11)]
print(numbers2)


pares = [i*2 for i in range(1,11) if i%2 == 0]
print(pares)