# Reading numbers from file and storing in a list using list comprehension method.

with open('number_list1.txt', mode='r') as file1:
    ## or num1_list = file1.readlines() ---> without list comprehension method.
    num1_list = [number.strip() for number in file1]

with open('number_list2.txt') as file2:
    ## or num2_list = file2.readlines() ---> without list comprehension method.
    num2_list = [number.strip() for number in file2]


# comparing two list numbers using list comprehension method.
result = [int(number) for num in num2_list for number in num1_list if num == number]
## or result = [int(number) for number in num1_list if number in num2_list]
print(result)