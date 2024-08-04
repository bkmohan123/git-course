some_list=['a','b','b','l','a','c']
duplicates=list(set([x for x in some_list if some_list.count(x)>1]))
print(duplicates)