def find_greatest(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        greatest=num1
    if num2 >= num1 and num2 >= num3:
        greatest=num2
    else:
        greatest=num3
    return greatest

num1=int(input("enter an number"))
num2=int(input("enter an number"))
num3=int(input("enter an number"))
great=find_greatest(num1,num2,num3)
print(great)