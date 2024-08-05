nums=[10,45,78,90,76]
largest=nums[0]
second_largest=nums[1]
for i in range(len(nums)):
    if nums[i]>largest:
        largest=nums[i]
for i in range(len(nums)):
    if nums[i]>second_largest and nums[i]!=largest:
        second_largest=nums[i]
print(second_largest)
