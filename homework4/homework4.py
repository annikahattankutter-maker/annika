numbers = list(range(0, 21)) # originally put range() not list(range())

def get_first_15(numbers):
    return numbers[:16]
print(get_first_15(numbers))

# ---- List Operations ----
fav_foods = ['pizza', 'tacos', 'enchiladas', 'tiramasu', 'beans']

print(fav_foods[-1]) # I put fav_food instead of fav_foods

fav_foods.append('goldfish')
print(fav_foods)

fav_foods.insert(0, 'apple')
print(fav_foods)

fav_foods.remove('tacos')
print(fav_foods)

print(len(fav_foods)) # I was using len[] not len()

for food in fav_foods:
    print(food.upper()) # was printing fav_foods.upper() not food.upper()

new_list = fav_foods[0::5]
print(new_list)

if 'potato' in fav_foods:
    print('A potato!')
else:
    print('No potato!')

# ---- Slicing and Striding ----
numbers = list(range(0, 21)) # originally put range() not list(range())

def get_first_15(numbers):
    return numbers[:16]
print(get_first_15(numbers))

def get_every_5th(first):
    return first[0::5]
print(get_every_5th(numbers))

def reverse_and_stride(first):
    first.reverse() # put a parameter in when it doesn't take parameters
    return first[::3]
print(reverse_and_stride(numbers))

# ---- Nested List Operations ----
numbers = [
    [1, 2, 3],  # forgot to put commas after each list in the nested list
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(numbers):
    total = 0
    for row in numbers: # was trying to add a list to an integer and it was angry with me
       for num in row:
           total += num # i put =+ instead of += and it gave me an output of 12
    return total
print(sum_nested(numbers))

# ---- Create a 5x5 List ----
def make_5x5():
    result = []
    num = 1
    for i in range(5):
        row = []
        for number in range(5):
            row.append(num)
            num += 1
        result.append(row)
    return result
nested_list = make_5x5()
print(nested_list)

def replace_with_3(nested):
    for num in range(len(nested)):
        for number in range(len(nested[num])):
            if nested[num][number] % 3 == 0:
                nested[num][number] = '?'
    return nested
print(replace_with_3(nested_list))

def not_question(nested):
    total = 0
    for row in range(len(nested)):
        for column in range(len(nested[row])):
            if nested[row][column] != '?':
                total += nested[row][column]
    return total
print(not_question(nested_list))

# ---- Dictionary Operations ----
ages = {
    'Katie': 30,
    'Mariam': 42,
    'Safia': 25,
    'Mira': 48
}

print(ages['Katie'])

ages['Mira'] = 100
print(ages['Mira'])

ages['Milana'] = 52
print(ages['Milana'])

for key, value in ages.items():
    print(key, value)

# python = 'Python'
# for letter in python:
#     print(letter)

# def print_characters(word):
#     for i in range(len(str(word))):
#         print(word[i])
# print_characters(word = 'Cherry')

# nums = [3, 7, 8, 2, 5]
# tracker = 0
# for i in nums:
#     if i > tracker:
#         tracker = i
# print(tracker)

# def compute_running_total(numbers):
#     totals = []
#     total = 0
#     for i in range(len(numbers)):
#         total += numbers[i]
#         totals.append(total)
#     return totals

# nums = [1, 2, 3, 4, 5]

# print(compute_running_total(nums))

# fruit ={'apple': 2, 'banana': 5, 'orange': 3}
# fruit.values()

# print(fruit['apple'])

# fruit['orange'] = 7
# print(fruit['orange'])

# print(fruit.values())
# fruit['date'] = 24

# for key in fruit.keys():
#     print(f"{key}")