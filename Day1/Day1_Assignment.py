#! Question – Widely Used Built-in Functions & Lambda

#&1. Uses range() to generate numbers from 1 to 20

# for i in range(1,21):
#     print(i)

#&2. Uses filter() with a lambda to select only even numbers

# numbers=[1,2,3,4,5,6,7,8,9,10]

# result=filter(lambda x:x%2==0,numbers)

# print(list(result))

#&3. Uses map() with a lambda to square the filtered numbers


# numbers=[1,2,3,4,5,6,7,8,9,10]

# result=map(lambda x:x*2,numbers)

# print(list(result))


#& 4. Uses reduce() to calculate the sum of squared even numbers

# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6]

# result = reduce(lambda x, y: x + y,map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
# )

# print(result)

#& 5. Uses enumerate() to print the index and value of the final result list

# final_result = [1, 2, 3]

# for index, value in enumerate(final_result):
#     print(index, value)


#!Question – List, Dictionary & Set Comprehensions

#& 1. Create a list comprehension to store squares of all numbers

# data = [1, 2, 3, 4, 5, 6, 2, 4]

# squares = [x**2 for x in data]

# print(squares)

#&2. Create a set comprehension to store only unique even numbers

# data = [1, 2, 3, 4, 5, 6, 2, 4]

# even_numbers = {x for x in data if x % 2 == 0}

# print(even_numbers)

#&3. Create a dictionary comprehension where the key is the number and the value is its cube

# data = [1, 2, 3, 4, 5, 6, 2, 4]

# cube_dict = {x: x**3 for x in data}

# print(cube_dict)