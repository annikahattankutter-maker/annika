# # 3.1 prints a goodbye message
# def say_goodbye():
#     print("Goodbye, see you later!")
# say_goodbye()

# # 3.2 prints the area of a circle with a given radius
# radius = 2
# def circle_area(given_radius):
#     area = given_radius ** 2
#     area_with_pi = area * 3.14
#     print(area_with_pi)
# circle_area(radius)

# a = 6
# b = 2
# #  4.1 subtracts b from a 
# def subtract(a, b):
#     return a - b
# print(subtract(a, b))

# # multiplies a and b
# def multiple(a, b):
#     return a * b
# print(multiple(a, b))

# # divides b from a
# def divide(a, b):
#     return 6 / 2
# print(divide(a, b))

# # 5.1 prints a grouping with the lowest and highest value from the list temperature
temperature = [77, 89, 72, 71, 76, 73, 69]
def highlow_temp(temp):
    temp_tuple = (min(temp), max(temp))
    print(temp_tuple)
highlow_temp(temperature)

# # 5.2 prints true or false depending on if a day of the week is a weekend
# sunday = 1
# monday = 2
# tuesday = 3
# wednesday = 4
# thursday = 5
# friday = 6
# saturday = 7
# def is_weekend(day):
#     if day == 1 or day == 7:
#         return True
#     else:
#         return False
# print(is_weekend(tuesday))

# # 5.3 determines the fuel effciency (miles per gallon) of a car
# miles = 120
# gallons = 5
# def which_car(distance, fuel):
#     return distance / fuel
# print(which_car(miles, gallons))

# # 5.4 returns a given numver with the last digit infront of the first digit
# def last_digit_switch(data):
#     if data < 10:
#         return data
#     last_digit = data % 10
#     rest = data // 10

#     multiplier = 1
#     temp = rest
#     while temp > 0:
#         multiplier *= 10
#         temp //= 10
    
#     encrypted = last_digit * multiplier + rest
#     return encrypted
# print(last_digit_switch(12345))

# # 6.1 uses a for loop ro raise x to the power of y
# def power(x, y):
#     result = 1
#     for num in range(y):
#         result *= x
#     return result
# print(power(3, 2))

# # 6.2.1 finds either the min or max value of a list without using the min() and max() commands
# def find_min(lst):
#     if not lst:
#         return None

#     min_value = lst[0]
#     for num in lst:
#         if num < min_value:
#             min_value = num
#     return min_value
# numbers = [5, 2, 9, 1, 7]
# print(find_min(numbers))

# def find_max(lst):
#     if len(lst) == 0:
#         return None

#     max_value = lst[0]
#     for num in lst:
#         if num > max_value:
#             max_value = num
#     return max_value
# numbers = [5, 2, 9, 1, 7]
# print(find_max(numbers))

# # 6.2.2 uses while liips to find the min or max value of a list
# def find_min(nums):
#     min_val = nums[0]
#     i = 1
#     while i < len(nums):
#         if nums[i] < min_val:
#             min_val = nums[i]
#         i += 1
#     return min_val
# nums = [4, 7, 2, 10, 0]
# print(find_min(nums))

# def find_max(nums):
#     max_val = nums[0]
#     i = 1
#     while i < len(nums):
#         if nums[i] > max_val:
#             max_val = nums[i]
#         i += 1 
#     return max_val

# nums = [4, 7, 2, 10, 0]
# print(find_max(nums))

# # 6.3 takes the last digit and adds it to the sum then removes the last digit and repeats
# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10      
#         total += digit      
#         n //= 10            
#     return total

# print(sum_of_digits(12345))






# # 5.1 prints a grouping with the lowest and highest value from the list temperature
# temperature = [77, 89, 72, 71, 76, 73, 69]
# def highlow_temp(temp):
#     temp_tuple = (min(temp), max(temp))
#     print(temp_tuple)
# highlow_temp(temperature)

temperature = [77, 89, 72, 71, 76, 73, 69]

def highlow_temp(temp):
    temp_tuple = (min(temp), max(temp))
    return temp_tuple   # return instead of print

result = highlow_temp(temperature)

print(f'The result of What Should I Wear (5.1) with temperature = {temperature} is {result}.')