import functools

numbers = [1, 2, 3, 4]

def acuum(counter, item):
    print('counter => ', counter)
    print('item => ', item)
    return counter + item

result = functools.reduce(acuum, numbers)
print(result)