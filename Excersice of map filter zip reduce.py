from functools import reduce
my_pets=['sisi','bibi','titi','carla']
def capitalize(my_pets):
    return my_pets.upper()
print(list(map(capitalize,my_pets)))
print(my_pets)

my_strings=['a','b','c','d','e']
your_number=[5,4,3,2,1]
print(list(zip(my_strings,sorted(your_number))))

function=[73,25,68,87,5,3]
def greater_50(item):
    return item>50
print(list(filter(greater_50,function)))

function=[73,25,68,87,5,3]
def accumalator(acc,function):
    print(acc,function)
    return (acc+function)
print(reduce(accumalator,function))


