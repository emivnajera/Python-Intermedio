numbers = [1,2,3,4]
numbers2 = []
numbers3 =  list(map(lambda i : i*2, numbers))

for i in numbers:
    numbers2.append(i*2)

print(numbers2)
print(numbers3)
