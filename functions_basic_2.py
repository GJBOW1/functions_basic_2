# Gregg Bowen - Functions Basic 2 Assignment 

# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    count = []
    for list in range(num,-1,-1):
        count.append(list)
    return count

countdown_fun = countdown(50)
print(countdown_fun)

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

def print_return (num):
    print(num[0])
    return num[1]

returned_num = print_return([2,5])
print(returned_num)
# you can use the above print function to confirm return worked in the function

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_length(num):
    sum = num[0] + len(num)
    return sum

returned_sum = first_length([5,4,3,2,1])
print(returned_sum)

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

def convert_list(num):
    new_list = []
    new_list.append(num[0])
    for i in range(0,len(num)):
        if i > num[2]:
            new_list.append(i)
    print(len(new_list))
    if len(new_list) <= 2:
        return False
    return new_list
    
converted_list = convert_list([9,3,4,5,0,1,4,6])
print(converted_list)

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_size(a,b): 
    value_list = []
    for i in range(a):
        value_list.append(b)
    return value_list

length_value = length_size(7,10)
print(length_value)