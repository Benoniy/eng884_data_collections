# What is a dictionary?
# Dictionaries use KEY, VALUE pairs to save data
# Data can be retrieved based on either its key or value
# {} is used to create a dictionary
# You can declare a list within a dictionary
dev_ops_students = {'key': 'value',
                    'name': 'Ben',
                    'stream': 'DevOps',
                    'completed_lessons': 3,
                    'completed_lessons_names': ['variables', 'data types', 'collections']
                    }


# How to retrieve data from a dictionary
# get a value based on a key
print(dev_ops_students['key'])


# dictionary methods
# add - to add a new key value pair to a dictionary you must explicitly state the new key and value
print(dev_ops_students)
dev_ops_students['new key'] = 'new value'
print(dev_ops_students)

# change - to change a key's value you must overwrite it similar to adding a new key value pair
print(dev_ops_students)
dev_ops_students['new key'] = 'changed value'
print(dev_ops_students)

# remove - to remove from a dictionary you must use the pop() method
print(dev_ops_students)
dev_ops_students.remove('key')
print(dev_ops_students)

