from functools import reduce

my_list=[1,2,3]
print(list(map(lambda my_list:my_list*2,my_list)))

my_list=[2,12,4,3,9]
print(list(filter(lambda my_list:my_list %2!=0,my_list)))

my_list=[1,2,3]
 print(reduce(lambda x,y:x*y,my_list))

