# Given an input List lst = [1, 2, 3, 4, 5]
# Write a business logic and print the same lst to give output as [1, 9, 25]

lst = [1, 2, 3, 4, 5]

result = [x**2 for x in lst if x % 2 != 0]
print(result)
