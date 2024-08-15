string=input("enter an string: ")
reversed_str=""
for char in string:
    #prepend character means the current character is hold in front of reverse_str
    reversed_str=char+reversed_str
print(reversed_str)