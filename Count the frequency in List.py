def count_frequency(numbers):
    frequency={}
    for num in numbers:
        if num in frequency:
            frequency[num]=frequency[num]+1
        else:
            frequency[num]=1
    return frequency
numbers=[1,2,3,4,5,1,2,4,5,2,3]
print(count_frequency(numbers))

