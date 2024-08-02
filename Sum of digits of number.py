'''def sum_of_digits(number):
    number_str=str(number)
    total=0
    for char in number_str:
        total=total+int(char)
    return total
number=int(input("enter an number"))
result=sum_of_digits(number)
print(result)'''

def sum_integer(num):
    total=0
    while(num>0):
        rem=num%10
        total=total+rem
        num=num//10

    return total
num=(int(input("enter an number")))
result=sum_integer(num)
print(result)