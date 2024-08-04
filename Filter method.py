num=[1,2,3,4,5]
def only_odd(num):
    return num %2 != 0
print(list(filter(only_odd,num)))
