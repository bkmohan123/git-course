from functools import reduce
my_list=[1,2,3,4]
def accumalator(acc,my_list):
    print(acc,my_list)
    return (acc+my_list )
print(reduce(accumalator,my_list))