# Lists and Tuples  

## Lists
### What is a list?  
  ***Lists are commonly used to store large amounts of data in a manageable format. Lists are***  
  ***mutable and they are created by using [].***  
```python
shopping_list = ['bread', 'milk', 'eggs', 'ham', 'apples']
```  

### How do we access specific items in a list?  
  ***Indexing works the same for lists as it does for strings, it starts at 0.***  
```python
['bread', 'milk', 'eggs', 'ham', 'apples']
    0        1       2      3       4

print(shopping_list[0]) -> 'bread'
```  
### List slicing  
  ***As with strings, lists can be 'sliced' to extract a sub list from a list. It works in much the same way***  
  ***as when strings are sliced.***  
```python
print(shopping_list[1:3]) -> ['milk', 'eggs']

print(shopping_list[-2])  -> ['ham']
```  
   
### List Methods  
  ***These methods can be used to manipulate a list or find information about it***  
* replace - to replace an item in a list you must explicitly overwrite it.  
```python
print(shopping_list) -> ['bread', 'milk', 'eggs', 'ham', 'apples']

shopping_list[0] = 'tomatoes'

print(shopping_list) -> ['tomatoes', 'milk', 'eggs', 'ham', 'apples']
```  
* append - to add an item to the end of a list you must use the append method.  
```python
print(shopping_list) -> ['bread', 'milk', 'eggs', 'ham', 'apples']

shopping_list.append('sausage')

print(shopping_list) -> ['bread', 'milk', 'eggs', 'ham', 'apples', 'sausage']
```  
* insert - to add an item to list at a specific index you must use the insert method. The object that is  
currently in that space will shifted up an index and so will all the objects with a higher index.  
```python
print(shopping_list) -> ['bread', 'milk', 'eggs', 'ham', 'apples']

shopping_list.insert(0, "avocado")

print(shopping_list) -> ['avocado', 'bread', 'milk', 'eggs', 'ham', 'apples']
```
* remove - to remove an object from a list when you know the content of the object.  
```python
print(shopping_list) -> ['bread', 'milk', 'eggs', 'ham', 'apples']

shopping_list.remove('eggs')

print(shopping_list) -> ['bread', 'milk', 'ham', 'apples']
```  
* pop - to remove an object from a list when you know the index of the object.  
```python
print(shopping_list) -> ['bread', 'milk', 'eggs', 'ham', 'apples']

shopping_list.pop(0)

print(shopping_list) -> ['milk', 'eggs', 'ham', 'apples']
```  

## Tuples  
### What is a Tuple?  
  ***A tuple is exactly the same as a list but there is one key difference, tuples are immutable.***  
  ***Because of this they should be used to store data that must never change in order to protect***  
  ***that data.***  
  
## Dictionaries  
### What is a dictionary?  
  ***Dictionaries use KEY, VALUE pairs to save data which can be retrieved based on either its***  
  ***key or value. They are created using {} and are so flexible that you can declare a list within one.***  
  ***keys must be unique!***
```python
dev_ops_students = {'key': 'value',
                    'name': 'Ben',
                    'stream': 'DevOps',
                    'completed_lessons': 3,
                    'completed_lessons_names': ['variables', 'data types', 'collections']  # This is a list declared as a value
                    }
```  
### How do you retrieve data from a dictionary?  
* To retrieve a value based on a key   
  `print(dev_ops_students['key']) -> 'value'`  
  
### Dictionary methods  
* add - to add a new key value pair to a dictionary you must explicitly state the new key and value
```python
print(dev_ops_students) -> {'key': 'value',
                            'name': 'Ben',
                            'completed_lessons': 3,
                            'completed_lessons_names': ['variables', 'data types', 'collections']
                            }

dev_ops_students['new key'] = 'new value'

print(dev_ops_students) -> {'key': 'value', 
                            'name': 'Ben', 
                            'completed_lessons': 3, 
                            'completed_lessons_names': ['variables', 'data types', 'collections'], 
                            'new key': 'new value'
                            }
```
* change - to change a key's value you must overwrite it similar to adding a new key value pair
```python
print(dev_ops_students) -> {'key': 'value', 
                            'name': 'Ben', 
                            'completed_lessons': 3, 
                            'completed_lessons_names': ['variables', 'data types', 'collections'], 
                            'new key': 'new value'
                            }

dev_ops_students['new key'] = 'changed value'

print(dev_ops_students) -> {'key': 'value', 
                            'name': 'Ben', 
                            'completed_lessons': 3, 
                            'completed_lessons_names': ['variables', 'data types', 'collections'], 
                            'new key': 'changed value'
                            }
```
* remove - to remove from a dictionary you must use the pop() method  
```python
print(dev_ops_students) -> {'key': 'value',
                            'name': 'Ben',
                            'completed_lessons': 3,
                            'completed_lessons_names': ['variables', 'data types', 'collections']
                            }

dev_ops_students.pop('key')

print(dev_ops_students) -> {'name': 'Ben',
                            'completed_lessons': 3,
                            'completed_lessons_names': ['variables', 'data types', 'collections']
                            }
```
