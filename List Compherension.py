'''my_list=[char for char in 'hello']
my_list2=[num*2 for num in range(0,100)]
my_list3=[num**2 for num in range(0,100) if num%2!=0]
print(my_list)
print(my_list3)'''
#list comprehensions offers concise way to create new list using existing list
my_list=[]
for char in 'heloo':
    my_list.append(char)
print(my_list)