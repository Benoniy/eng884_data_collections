# What is a list
# Lists are commonly used to store large amounts of data
# Lists are mutable
# [] is used to create a list
shopping_list = ['bread', 'milk', 'eggs', 'ham', 'apples']

# Indexing works the same as with strings
# 'bread', 'milk', 'eggs', 'ham', 'apples'
#    0        1       2      3       4
print(shopping_list[0])

# You can slice a list in the exact same way you would slice a string, this includes reverse slicing
print(shopping_list[1:3])
print(shopping_list[-2])


# To replace something in a list you explicitly overwrite it
print(shopping_list)
shopping_list[0] = 'tomatoes'
print(shopping_list)

# To add something to a list you should use .append() or .insert if using an index
print(shopping_list)
shopping_list.append('sausage')
print(shopping_list)
shopping_list.insert(0, "avocado")
print(shopping_list)

# To delete something from a list you should use .remove() or .pop() if using the index
print(shopping_list)
shopping_list.remove('eggs')
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

