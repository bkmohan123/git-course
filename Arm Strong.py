num=int(input("enter an number"))
res=0
digit=len(str(num))
temp=num
while(num>0):
    rem=num%10
    res=(rem**digit)+res
    num=num//10
print(res)

if res==temp:
    print("it is arm strong")
else:
    print("not an arm strong")
