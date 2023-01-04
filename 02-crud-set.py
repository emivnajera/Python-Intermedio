set_countries = {'gt','mex','col'}

size = len(set_countries)
print(size)

print('gt' in set_countries)
print('usa' in set_countries)

#add
set_countries.add('usa')
set_countries.add('usa')

print('usa' in set_countries)
print(set_countries)

#update
set_countries.update({'ar','br','ec'})
print(set_countries)

#remove
set_countries.remove('col')
print(set_countries)


set_countries.clear()
print(set_countries)