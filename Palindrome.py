num=int(input("enter an number"))
res=0
temp=num
while(num>0):
    rem=num%10
    res=(res*10)+rem
    num=num//10
print(res)
if(res==temp):
    print("num is palindrome")
else:
    print("num is not palindrome")