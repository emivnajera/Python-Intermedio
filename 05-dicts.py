import random

dict = {}

for i in range(1,5):
    dict[i] = i * 2

print(dict)

dict2 = {i: i * 2 for i in range(1,5)}
print(dict2)
#########
countries = ['col', 'mex', 'gt']
population = {}
for country in countries:
    for country in countries:
        population[country] = random.randint(1,100)
print(population)

population2 = { country: random.randint(1,100) for country in countries}
print(population2)


result = {country: population for (country,population) in population2.items() if population > 50}
print(result)