def reverse_number(num,res=0):
    if num==0:
        return res
    rem=num%10
    res=(res*10)+rem
    return reverse_number(num//10,res)
def is_palindrome(num):
    reversed=reverse_number(num)
    if num==reversed:
        return True
    else:
        return False
num=int(input("enter an number"))
if is_palindrome(num):
    print(f"{num} is an palindrome ")
else:
    print(f"{num} not a palindrome")